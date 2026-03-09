#!/usr/bin/env python3
"""
Baixa imagens educacionais do Wikimedia Commons para as aulas
de Analise de Dados Ambientais.
Uso educacional/didatico (nao comercial).
"""
import os
import json
import time
import urllib.request
import urllib.parse
import ssl

# Desabilitar verificacao SSL apenas para download educacional
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE = os.path.dirname(os.path.abspath(__file__))

# ========== MAPEAMENTO: pasta -> lista de (nome_arquivo_commons, nome_local) ==========
IMAGENS = {
    # --- CORRELACAO ---
    "correlacao": [
        ("Soil_sampling_in_field_East_of_Upholland_Road_-_geograph.org.uk_-_5739011.jpg",
         "foto_coleta_solo_campo.jpg"),
        ("CSIRO_ScienceImage_209_Taking_a_Sample_of_Soil_From_a_Rice_Field.jpg",
         "foto_amostragem_solo_arroz.jpg"),
        ("Weather_Monitoring_Station.jpg",
         "foto_estacao_monitoramento.jpg"),
    ],
    # --- REGRESSAO ---
    "regressao": [
        ("No-till_farming_system_in_Brookings,_Co.,_SD_(13873991983).jpg",
         "foto_plantio_direto.jpg"),
        ("Crop-rotation.JPG",
         "foto_rotacao_culturas.jpg"),
        ("Soybeans_no-till.jpg",
         "foto_soja_plantio_direto.jpg"),
        ("Awesome_Cover_Crops_started_in_Eastern_South_Dakota_(14941079819).jpg",
         "foto_cobertura_vegetal.jpg"),
    ],
    # --- NAO PARAMETRICOS ---
    "nao_parametricos": [
        ("Soybean_Field_with_Healthy_Soil_(9316804120).jpg",
         "foto_campo_soja_solo.jpg"),
        ("Agriculture_Research_Service_(ARS)_(8424937828).jpg",
         "foto_pesquisa_agricola.jpg"),
    ],
    # --- TRI INTRODUCAO ---
    "tri_introducao": [
        ("Wartime_Social_Survey-_Information_Gathering_in_Wartime_Britain,_UK,_1944_D18860.jpg",
         "foto_pesquisa_survey.jpg"),
    ],
    # --- DETECCAO ANOMALIAS ---
    "deteccao_anomalias": [
        ("Weather_Station_2015.jpg",
         "foto_estacao_meteorologica.jpg"),
        ("250mm_Rain_Gauge.jpg",
         "foto_pluviometro.jpg"),
        ("Rain_gauge_Hellmann.jpg",
         "foto_pluviometro_hellmann.jpg"),
        ("Ena_Rain_gauge_station.jpg",
         "foto_estacao_pluviometrica.jpg"),
    ],
    # --- BOOTSTRAPPING ---
    "bootstrapping": [
        ("No-till_Planting_(8120028117).jpg",
         "foto_plantio_campo.jpg"),
    ],
    # --- INTRODUCAO ETIMOLOGIA ---
    "introducao_etimologia": [
        ("NRCSCA00045_-_California_(589)(NRCS_Photo_Gallery).jpg",
         "foto_pesquisa_campo_california.jpg"),
    ],
    # --- ESTATISTICA DESCRITIVA ---
    "estatistica_descritiva": [
        ("Agriculture_Research_Service_(ARS)_(8412966436).jpg",
         "foto_laboratorio_pesquisa.jpg"),
    ],
}


def get_commons_url(filename, thumb_width=1280):
    """Obtem URL de thumbnail do Wikimedia Commons via API (respeita rate limit)."""
    api_url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": f"File:{filename}",
        "prop": "imageinfo",
        "iiprop": "url|size",
        "iiurlwidth": str(thumb_width),
        "format": "json",
    }
    url = api_url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "User-Agent": "EducationalDownloader/1.0 (UEFS; didactic use; contact ldvsantos@uefs.br)"
    })
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        pages = data.get("query", {}).get("pages", {})
        for page_id, page_data in pages.items():
            imageinfo = page_data.get("imageinfo", [])
            if imageinfo:
                # Prefere thumbnail (menor, menos rate-limit)
                thumb_url = imageinfo[0].get("thumburl")
                if thumb_url:
                    return thumb_url
                return imageinfo[0].get("url")
    except Exception as e:
        print(f"  ERRO API para {filename}: {e}")
    return None


def download_image(url, dest_path):
    """Baixa uma imagem de uma URL para o caminho de destino."""
    req = urllib.request.Request(url, headers={
        "User-Agent": "EducationalDownloader/1.0 (UEFS; didactic use; contact ldvsantos@uefs.br)"
    })
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
            with open(dest_path, "wb") as f:
                f.write(resp.read())
        return True
    except Exception as e:
        print(f"  ERRO download: {e}")
        return False


def main():
    total = sum(len(imgs) for imgs in IMAGENS.values())
    baixadas = 0
    erros = 0
    puladas = 0

    print(f"=== Iniciando download de {total} imagens educacionais ===\n")

    for pasta, imagens in IMAGENS.items():
        dest_dir = os.path.join(BASE, pasta)
        if not os.path.isdir(dest_dir):
            print(f"[AVISO] Pasta nao encontrada: {pasta}")
            continue

        print(f"\n--- {pasta} ({len(imagens)} imagens) ---")

        for commons_name, local_name in imagens:
            dest_path = os.path.join(dest_dir, local_name)

            if os.path.exists(dest_path):
                print(f"  [PULAR] {local_name} (ja existe)")
                puladas += 1
                continue

            print(f"  [BUSCAR] {commons_name}")
            url = get_commons_url(commons_name)

            if not url:
                print(f"  [FALHA] Nao encontrou URL para: {commons_name}")
                erros += 1
                continue

            print(f"  [BAIXAR] {local_name}")
            if download_image(url, dest_path):
                size_kb = os.path.getsize(dest_path) / 1024
                print(f"  [OK] {local_name} ({size_kb:.0f} KB)")
                baixadas += 1
            else:
                erros += 1

            time.sleep(3)  # respeitar rate limit (3s entre downloads)

    print(f"\n=== RESUMO ===")
    print(f"  Baixadas: {baixadas}")
    print(f"  Puladas:  {puladas}")
    print(f"  Erros:    {erros}")
    print(f"  Total:    {total}")


if __name__ == "__main__":
    main()
