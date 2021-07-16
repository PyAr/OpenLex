import pytest

@pytest.mark.skip(reason="Este test funciona en local pero falla en github, no toma el evento download")   
def test_download(page, login):
    page.goto("expedientes/index")
    page.click("text=Movimientos")
    with page.expect_download() as download_info:
        # Perform the action that initiates download
        page.click("text=Descarga")
    download = download_info.value
    # Wait for the download process to complete
    name = download.suggested_filename
    assert "Movimiento.zip" == name
    
    
