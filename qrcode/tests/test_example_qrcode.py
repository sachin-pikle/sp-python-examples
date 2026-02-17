import io
import os
import subprocess

import qrcode


def test_make_returns_pil_image():
    img = qrcode.make("hello")
    from qrcode.image.pil import PilImage

    assert isinstance(img, PilImage)


essential_png_sig = b"\x89PNG\r\n\x1a\n"


def test_make_save_to_bytesio_roundtrip_png():
    img = qrcode.make("data")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    data = buf.getvalue()
    assert data.startswith(essential_png_sig)
    assert len(data) > 100


def test_qrcode_svg_fragment_output():
    from qrcode.image.svg import SvgFragmentImage

    qr = qrcode.QRCode(image_factory=SvgFragmentImage)
    qr.add_data("abc123")
    img = qr.make_image()
    out = io.BytesIO()
    img.save(out)
    blob = out.getvalue()
    assert blob.lstrip().startswith(b"<svg")


def test_cli_qr_writes_png_when_output_path_given(tmp_path):
    qr_path = os.path.join(os.getcwd(), ".venv", "bin", "qr")
    assert os.path.exists(qr_path), "qr console script not found in venv"

    out_file = tmp_path / "out.png"
    res = subprocess.run(
        [qr_path, "--output", str(out_file), "hello"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert res.returncode == 0
    blob = out_file.read_bytes()
    assert blob.startswith(essential_png_sig)
    assert len(blob) > 100


def test_cli_qr_emits_png_to_stdout_when_piped():
    qr_path = os.path.join(os.getcwd(), ".venv", "bin", "qr")
    assert os.path.exists(qr_path), "qr console script not found in venv"

    res = subprocess.run(
        [qr_path, "hello"],
        check=True,
        capture_output=True,
        text=False,
    )
    assert res.returncode == 0
    assert res.stdout.startswith(essential_png_sig)
    assert len(res.stdout) > 100
