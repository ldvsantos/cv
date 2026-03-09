## ================================================================
## Script para gerar figuras dos módulos Poisson e Sobrevida
## ================================================================

library(ggplot2)
library(survival)
library(survminer)
library(MASS)

# Tema padrão para todas as figuras
tema <- theme_minimal(base_size = 16) +
  theme(
    plot.title = element_text(face = "bold", hjust = 0.5, size = 18),
    plot.subtitle = element_text(hjust = 0.5, color = "grey40"),
    legend.position = "bottom",
    panel.grid.minor = element_blank()
  )

# ================================================================
# DECK 1: Regressão de Poisson
# ================================================================
dir.create("regressao_poisson", showWarnings = FALSE)

## Fig 1 — Distribuição de Poisson com diferentes lambda
set.seed(42)
x <- 0:20
df_pois <- data.frame(
  x = rep(x, 4),
  prob = c(dpois(x, 1), dpois(x, 3), dpois(x, 5), dpois(x, 10)),
  lambda = factor(rep(c("lambda == 1", "lambda == 3",
                         "lambda == 5", "lambda == 10"), each = length(x)),
                  levels = c("lambda == 1", "lambda == 3",
                             "lambda == 5", "lambda == 10"))
)

p1 <- ggplot(df_pois, aes(x = x, y = prob, fill = lambda)) +
  geom_col(width = 0.7, show.legend = FALSE) +
  facet_wrap(~ lambda, labeller = label_parsed, scales = "free_y") +
  labs(
    title = expression("Distribuição de Poisson para diferentes valores de" ~ lambda),
    x = "Número de eventos (k)",
    y = "P(X = k)"
  ) + tema

ggsave("regressao_poisson/fig_01_distribuicao_poisson.png",
       p1, width = 10, height = 6, dpi = 200, bg = "white")

## Fig 2 — Histograma de dados de contagem (assimetria à direita)
set.seed(42)
contagem <- rpois(500, lambda = 2.5)
df_hist <- data.frame(contagem = contagem)

p2 <- ggplot(df_hist, aes(x = contagem)) +
  geom_histogram(binwidth = 1, fill = "#2196F3", color = "white",
                 boundary = -0.5) +
  geom_vline(aes(xintercept = mean(contagem)),
             linetype = "dashed", color = "red", linewidth = 1) +
  annotate("text", x = mean(contagem) + 0.8, y = max(table(contagem)) * 0.9,
           label = paste0("Média = ", round(mean(contagem), 2),
                          "\nVar = ", round(var(contagem), 2)),
           hjust = 0, size = 5, color = "red") +
  labs(
    title = "Distribuição típica de dados de contagem",
    subtitle = expression("Dados simulados — Poisson(" * lambda * " = 2,5)"),
    x = "Número de eventos",
    y = "Frequência"
  ) + tema

ggsave("regressao_poisson/fig_02_histograma_contagem.png",
       p2, width = 8, height = 5, dpi = 200, bg = "white")

## Fig 3 — Diagrama link log: relação entre preditores e contagem
set.seed(42)
x_pred <- seq(0, 5, length.out = 100)
y_link <- exp(0.5 + 0.4 * x_pred)  # predição do modelo Poisson
dados_sim <- data.frame(x = runif(200, 0, 5))
dados_sim$y <- rpois(200, lambda = exp(0.5 + 0.4 * dados_sim$x))
df_link <- data.frame(x = x_pred, y = y_link)

p3 <- ggplot() +
  geom_point(data = dados_sim, aes(x = x, y = y),
             alpha = 0.4, color = "#666666", size = 2) +
  geom_line(data = df_link, aes(x = x, y = y),
            color = "#E91E63", linewidth = 1.5) +
  labs(
    title = "Regressão de Poisson: relação exponencial",
    subtitle = expression("log(" * mu * ") = " * beta[0] + beta[1] * X
                          %->% mu == e^{beta[0] + beta[1] * X}),
    x = "Variável preditora (X)",
    y = "Contagem esperada (Y)"
  ) + tema

ggsave("regressao_poisson/fig_03_link_log.png",
       p3, width = 8, height = 5, dpi = 200, bg = "white")

cat("✓ Deck 1: 3 figuras geradas\n")

# ================================================================
# DECK 2: Superdispersão e Binomial Negativa
# ================================================================
dir.create("regressao_poisson", showWarnings = FALSE)

## Fig 1 — Equidispersão vs. Superdispersão
set.seed(42)
n <- 500
equi <- rpois(n, lambda = 5)
super <- rnbinom(n, mu = 5, size = 1.5)
df_disp <- data.frame(
  valor = c(equi, super),
  tipo = rep(c("Poisson (equidisperso)", "Binomial Negativa (superdisperso)"), each = n)
)

p4 <- ggplot(df_disp, aes(x = valor, fill = tipo)) +
  geom_histogram(binwidth = 1, color = "white", boundary = -0.5) +
  facet_wrap(~ tipo, ncol = 1, scales = "free_y") +
  scale_fill_manual(values = c("#2196F3", "#FF5722")) +
  labs(
    title = "Equidispersão vs. Superdispersão",
    subtitle = expression("Ambos com" ~ mu == 5 ~
                          "— note a cauda mais pesada na binomial negativa"),
    x = "Número de eventos",
    y = "Frequência"
  ) + tema + theme(legend.position = "none")

ggsave("regressao_poisson/fig_01_equidispersao_superdispersao.png",
       p4, width = 8, height = 7, dpi = 200, bg = "white")

## Fig 2 — Relação média-variância: Poisson vs BN
set.seed(42)
medias <- seq(1, 20, by = 1)
df_mv <- data.frame(
  media = rep(medias, 2),
  variancia = c(medias, medias + 0.8 * medias^2),
  modelo = rep(c("Poisson: Var = μ",
                 "Binomial Negativa: Var = μ + αμ²"), each = length(medias))
)

p5 <- ggplot(df_mv, aes(x = media, y = variancia, color = modelo)) +
  geom_line(linewidth = 1.5) +
  geom_point(size = 2.5) +
  scale_color_manual(values = c("#FF5722", "#2196F3")) +
  labs(
    title = "Relação Média–Variância",
    subtitle = "Na Poisson a variância acompanha a média;\nna Binomial Negativa, cresce mais rápido",
    x = expression("Média (" * mu * ")"),
    y = expression("Variância")
  ) + tema + theme(legend.title = element_blank())

ggsave("regressao_poisson/fig_02_media_variancia.png",
       p5, width = 9, height = 5.5, dpi = 200, bg = "white")

cat("✓ Deck 2: 2 figuras geradas\n")

# ================================================================
# DECK 3: Poisson Robusta
# ================================================================

## Fig 1 — OR vs RP por prevalência do desfecho
prev <- seq(0.05, 0.60, by = 0.01)
rp_real <- 2.0
or_approx <- (rp_real * (1 - prev * rp_real / (rp_real))) /
  (1 - prev)
# Derivação correta: dado RP=2, prevalência p nos não-expostos
# prevalência 2p nos expostos
# OR = (2p/(1-2p)) / (p/(1-p)) = 2(1-p)/(1-2p)
or_calc <- sapply(prev, function(p0) {
  p1 <- rp_real * p0
  if (p1 >= 1) return(NA)
  (p1 / (1 - p1)) / (p0 / (1 - p0))
})

df_or_rp <- data.frame(
  prevalencia = prev * 100,
  OR = or_calc,
  RP = rp_real
)

p6 <- ggplot(df_or_rp, aes(x = prevalencia)) +
  geom_line(aes(y = OR, color = "Odds Ratio (OR)"), linewidth = 1.5) +
  geom_hline(aes(yintercept = RP, color = "Razão de Prevalência (RP)"),
             linetype = "dashed", linewidth = 1.5) +
  scale_color_manual(values = c("Odds Ratio (OR)" = "#E91E63",
                                "Razão de Prevalência (RP)" = "#2196F3")) +
  coord_cartesian(ylim = c(1, 10)) +
  labs(
    title = "Divergência entre OR e RP conforme a prevalência",
    subtitle = "RP real = 2,0 — a OR superestima o efeito quando o desfecho é frequente",
    x = "Prevalência do desfecho no grupo não exposto (%)",
    y = "Magnitude da medida de associação"
  ) + tema + theme(legend.title = element_blank())

ggsave("regressao_poisson/fig_01_or_vs_rp.png",
       p6, width = 9, height = 5.5, dpi = 200, bg = "white")

## Fig 2 — IC padrão vs IC robusto
set.seed(42)
vars <- c("Sexo (F vs M)", "Idade (>60)", "Obesidade", "Tabagismo", "Diabetes")
rp_vals <- c(1.72, 1.15, 2.10, 1.85, 0.65)
ic_padrao_lo <- c(1.50, 0.98, 1.85, 1.62, 0.52)
ic_padrao_hi <- c(1.97, 1.35, 2.38, 2.11, 0.81)
ic_robusto_lo <- c(1.28, 0.82, 1.55, 1.30, 0.40)
ic_robusto_hi <- c(2.31, 1.61, 2.84, 2.63, 1.06)

df_ic <- data.frame(
  variavel = rep(vars, 2),
  RP = rep(rp_vals, 2),
  lo = c(ic_padrao_lo, ic_robusto_lo),
  hi = c(ic_padrao_hi, ic_robusto_hi),
  tipo = rep(c("IC Padrão (Poisson)", "IC Robusto (Sanduíche)"), each = 5)
)
df_ic$variavel <- factor(df_ic$variavel, levels = rev(vars))

p7 <- ggplot(df_ic, aes(x = RP, y = variavel, color = tipo)) +
  geom_vline(xintercept = 1, linetype = "dashed", color = "grey50") +
  geom_errorbarh(aes(xmin = lo, xmax = hi),
                 height = 0.3, linewidth = 1,
                 position = position_dodge(width = 0.6)) +
  geom_point(size = 3, position = position_dodge(width = 0.6)) +
  scale_color_manual(values = c("#2196F3", "#FF5722")) +
  labs(
    title = "IC Padrão vs. IC Robusto (Sanduíche de Huber-White)",
    subtitle = "Erros-padrão robustos produzem ICs geralmente mais largos e honestos",
    x = "Razão de Prevalência (RP)",
    y = NULL
  ) + tema + theme(legend.title = element_blank())

ggsave("regressao_poisson/fig_02_ic_padrao_vs_robusto.png",
       p7, width = 10, height = 5.5, dpi = 200, bg = "white")

cat("✓ Deck 3: 2 figuras geradas\n")

# ================================================================
# DECK 4: Análise de Sobrevida
# ================================================================
dir.create("analise_sobrevida", showWarnings = FALSE)

## Fig 1 — Diagrama de censura (swimmers plot)
set.seed(42)
n_pac <- 12
entrada <- rep(0, n_pac)
tempos <- c(5, 8, 12, 3, 15, 10, 7, 18, 6, 14, 11, 9)
status <- c(1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1)

df_swim <- data.frame(
  paciente = factor(paste0("Pac ", 1:n_pac), levels = paste0("Pac ", n_pac:1)),
  tempo = tempos,
  status = factor(status, labels = c("Censurado", "Evento"))
)

p8 <- ggplot(df_swim, aes(y = paciente)) +
  geom_segment(aes(x = 0, xend = tempo, yend = paciente),
               linewidth = 2, color = "#607D8B") +
  geom_point(aes(x = tempo, shape = status, color = status), size = 4) +
  scale_shape_manual(values = c("Censurado" = 3, "Evento" = 16)) +
  scale_color_manual(values = c("Censurado" = "#2196F3", "Evento" = "#E91E63")) +
  labs(
    title = "Representação do acompanhamento em Análise de Sobrevida",
    subtitle = "Cada linha = um paciente | ● = evento | + = censura",
    x = "Tempo de acompanhamento (meses)",
    y = NULL,
    shape = NULL, color = NULL
  ) + tema

ggsave("analise_sobrevida/fig_01_swimmers_plot.png",
       p8, width = 9, height = 5.5, dpi = 200, bg = "white")

## Fig 2 — Curva de Kaplan-Meier (amostra única)
set.seed(42)
n_km <- 100
tempo_km <- rexp(n_km, rate = 0.05)
cens_km <- runif(n_km, 0, 40)
tempo_obs <- pmin(tempo_km, cens_km)
status_km <- as.integer(tempo_km <= cens_km)
df_km <- data.frame(tempo = tempo_obs, status = status_km)

km_fit <- survfit(Surv(tempo, status) ~ 1, data = df_km)

p9 <- ggsurvplot(km_fit,
                 data = df_km,
                 conf.int = TRUE,
                 risk.table = TRUE,
                 risk.table.col = "strata",
                 ggtheme = theme_minimal(base_size = 14),
                 palette = "#2196F3",
                 xlab = "Tempo (meses)",
                 ylab = "Probabilidade de sobrevida S(t)",
                 title = "Curva de Kaplan-Meier",
                 subtitle = "Com intervalo de confiança de 95% e tabela de risco",
                 surv.median.line = "hv",
                 censor.shape = "+",
                 censor.size = 3)

png("analise_sobrevida/fig_02_kaplan_meier.png",
    width = 2000, height = 1400, res = 200)
print(p9)
dev.off()

## Fig 3 — Curva KM por grupos + log-rank
set.seed(42)
n_g <- 80
grupo <- rep(c("Tratamento A", "Tratamento B"), each = n_g)
tempo_g <- c(rexp(n_g, rate = 0.03), rexp(n_g, rate = 0.07))
cens_g <- runif(2 * n_g, 0, 35)
tempo_obs_g <- pmin(tempo_g, cens_g)
status_g <- as.integer(tempo_g <= cens_g)
df_g <- data.frame(tempo = tempo_obs_g, status = status_g, grupo = grupo)

km_g <- survfit(Surv(tempo, status) ~ grupo, data = df_g)

p10 <- ggsurvplot(km_g,
                  data = df_g,
                  pval = TRUE,
                  conf.int = TRUE,
                  risk.table = TRUE,
                  ggtheme = theme_minimal(base_size = 14),
                  palette = c("#2196F3", "#E91E63"),
                  xlab = "Tempo (meses)",
                  ylab = "Probabilidade de sobrevida S(t)",
                  title = "Comparação de curvas de sobrevida",
                  subtitle = "Teste log-rank (Mantel-Cox)",
                  legend.title = "Grupo",
                  censor.shape = "+",
                  censor.size = 3)

png("analise_sobrevida/fig_03_kaplan_meier_grupos.png",
    width = 2000, height = 1400, res = 200)
print(p10)
dev.off()

cat("✓ Deck 4: 3 figuras geradas\n")

# ================================================================
# DECK 5: Regressão de Cox
# ================================================================

## Fig 1 — Forest Plot
set.seed(42)
n_cox <- 200
df_cox <- data.frame(
  tempo = rexp(n_cox, rate = 0.04),
  sexo = factor(sample(c("Masculino", "Feminino"), n_cox, replace = TRUE)),
  idade_60 = factor(sample(0:1, n_cox, replace = TRUE, prob = c(0.6, 0.4)),
                    labels = c("< 60 anos", "≥ 60 anos")),
  estadio = factor(sample(1:3, n_cox, replace = TRUE, prob = c(0.4, 0.35, 0.25)),
                   labels = c("I", "II", "III")),
  tratamento = factor(sample(c("Convencional", "Experimental"), n_cox, replace = TRUE))
)
# Modular hazard por covariáveis
mult <- rep(1, n_cox)
mult[df_cox$sexo == "Feminino"] <- mult[df_cox$sexo == "Feminino"] * 0.75
mult[df_cox$idade_60 == "≥ 60 anos"] <- mult[df_cox$idade_60 == "≥ 60 anos"] * 1.8
mult[df_cox$estadio == "II"] <- mult[df_cox$estadio == "II"] * 1.5
mult[df_cox$estadio == "III"] <- mult[df_cox$estadio == "III"] * 2.5
mult[df_cox$tratamento == "Experimental"] <- mult[df_cox$tratamento == "Experimental"] * 0.6
df_cox$tempo <- df_cox$tempo / mult
cens_cox <- runif(n_cox, 0, 40)
df_cox$tempo_obs <- pmin(df_cox$tempo, cens_cox)
df_cox$status <- as.integer(df_cox$tempo <= cens_cox)

cox_multi <- coxph(Surv(tempo_obs, status) ~ sexo + idade_60 + estadio + tratamento,
                   data = df_cox)

p11 <- ggforest(cox_multi, data = df_cox,
                main = "Forest Plot — Regressão de Cox Multivariada",
                fontsize = 1.0)

ggsave("analise_sobrevida/fig_01_forest_plot.png",
       p11, width = 10, height = 6, dpi = 200, bg = "white")

## Fig 2 — Resíduos de Schoenfeld
ph_test <- cox.zph(cox_multi)
png("analise_sobrevida/fig_02_schoenfeld.png",
    width = 2000, height = 1600, res = 200)
par(mfrow = c(2, 2), mar = c(4, 4, 3, 1))
for (i in seq_len(min(4, ncol(ph_test$y)))) {
  plot(ph_test[i], main = colnames(ph_test$y)[i],
       xlab = "Tempo", ylab = "Beta(t) para resíduos de Schoenfeld")
  abline(h = 0, col = "red", lty = 2)
}
dev.off()

## Fig 3 — Curvas de sobrevida ajustadas por grupo de tratamento
p12 <- ggadjustedcurves(cox_multi,
                        variable = "tratamento",
                        data = df_cox,
                        ggtheme = theme_minimal(base_size = 14),
                        palette = c("#2196F3", "#E91E63"))

p12 <- p12 + labs(
  title = "Curvas de sobrevida ajustadas — Regressão de Cox",
  subtitle = "Ajustadas por sexo, idade e estadiamento",
  x = "Tempo (meses)",
  y = "Probabilidade de sobrevida S(t)",
  color = "Tratamento"
)

ggsave("analise_sobrevida/fig_03_curvas_ajustadas.png",
       p12, width = 9, height = 5.5, dpi = 200, bg = "white")

cat("✓ Deck 5: 3 figuras geradas\n")
cat("\n=== TODAS AS FIGURAS GERADAS COM SUCESSO ===\n")
