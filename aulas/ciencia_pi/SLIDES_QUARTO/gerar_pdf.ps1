# Script para gerar PDF da apresentação Reveal.js usando DeckTape
# Este script primeiro renderiza o HTML com Quarto e depois converte para PDF

$apresentacaoQmd = "tema07_apresentacao.qmd"
$apresentacaoHtml = "tema07_apresentacao.html"
$pdfOutput = "tema07_apresentacao.pdf"

# Caminho completo
$caminhoQmd = Join-Path $PSScriptRoot $apresentacaoQmd
$caminhoHtml = Join-Path $PSScriptRoot $apresentacaoHtml
$pdfCompleto = Join-Path $PSScriptRoot $pdfOutput

Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "Script de Geração de PDF - Tema 07" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Verifica se o arquivo .qmd existe
if (-not (Test-Path $caminhoQmd)) {
    Write-Host "ERRO: Arquivo $apresentacaoQmd não encontrado!" -ForegroundColor Red
    exit 1
}

# Etapa 1: Renderizar HTML com Quarto
Write-Host "[1/3] Renderizando HTML com Quarto..." -ForegroundColor Yellow
Write-Host ""

try {
    quarto render $caminhoQmd
    if ($LASTEXITCODE -ne 0) {
        Write-Host "ERRO: Falha ao renderizar o arquivo Quarto." -ForegroundColor Red
        exit 1
    }
    Write-Host "HTML renderizado com sucesso!" -ForegroundColor Green
} catch {
    Write-Host "ERRO ao executar Quarto: $_" -ForegroundColor Red
    Write-Host "Certifique-se de que o Quarto está instalado: https://quarto.org/docs/get-started/" -ForegroundColor Yellow
    exit 1
}

Start-Sleep -Seconds 1
Write-Host ""

# Verifica se o HTML foi criado
if (-not (Test-Path $caminhoHtml)) {
    Write-Host "ERRO: HTML não foi gerado. Verifique erros no arquivo .qmd" -ForegroundColor Red
    exit 1
}

# Etapa 2: Verificar Node.js
Write-Host "[2/3] Verificando dependências..." -ForegroundColor Yellow

try {
    $nodeVersion = node --version 2>$null
    if ($nodeVersion) {
        Write-Host "Node.js encontrado: $nodeVersion" -ForegroundColor Green
    }
} catch {
    Write-Host "ERRO: Node.js não encontrado." -ForegroundColor Red
    Write-Host "Por favor, instale o Node.js de https://nodejs.org/" -ForegroundColor Yellow
    exit 1
}

# Verifica se o DeckTape está instalado globalmente
$deckTapeInstalled = $false
try {
    $null = Get-Command decktape -ErrorAction Stop
    $deckTapeInstalled = $true
    Write-Host "DeckTape já instalado." -ForegroundColor Green
} catch {
    Write-Host "DeckTape não encontrado. Instalando..." -ForegroundColor Yellow
    npm install -g decktape
    if ($LASTEXITCODE -eq 0) {
        $deckTapeInstalled = $true
        Write-Host "DeckTape instalado com sucesso!" -ForegroundColor Green
    } else {
        Write-Host "ERRO ao instalar DeckTape." -ForegroundColor Red
        exit 1
    }
}

Write-Host ""

# Etapa 3: Gerar PDF
if ($deckTapeInstalled) {
    Write-Host "[3/3] Gerando PDF da apresentação..." -ForegroundColor Yellow
    Write-Host ""
    
    # Usa DeckTape para gerar o PDF
    $fileUrl = "file:///$($caminhoHtml.Replace('\', '/'))"
    
    Write-Host "Convertendo: $apresentacaoHtml -> $pdfOutput" -ForegroundColor Cyan
    decktape reveal $fileUrl $pdfCompleto --size 1280x720
    
    Start-Sleep -Seconds 2
    
    if (Test-Path $pdfCompleto) {
        Write-Host ""
        Write-Host "===============================================" -ForegroundColor Green
        Write-Host "PDF gerado com sucesso!" -ForegroundColor Green
        Write-Host "Localização: $pdfCompleto" -ForegroundColor Green
        Write-Host "===============================================" -ForegroundColor Green
        
        # Abre o PDF automaticamente
        Write-Host ""
        Write-Host "Abrindo o PDF..." -ForegroundColor Cyan
        Start-Process $pdfCompleto
    } else {
        Write-Host "ERRO: PDF não foi criado." -ForegroundColor Red
        Write-Host "Verifique se há erros no console acima." -ForegroundColor Yellow
        exit 1
    }
} else {
    Write-Host "ERRO: DeckTape não está disponível." -ForegroundColor Red
    exit 1
}
