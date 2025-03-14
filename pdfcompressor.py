import os
import subprocess

input_pdf_path = r""
output_pdf_path = r""
ghostscript_path = r"C:\Program Files\gs\gs10.05.0\bin\gswin64c.exe"

max_size_mb = 1.8
max_size_bytes = max_size_mb * 1024 * 1024 

compression_levels = ["/screen", "/ebook", "/printer", "/prepress"]

for level in compression_levels:
    print(f"Applying Ghostscript compression: {level}")
    
    gs_command = [
        ghostscript_path,
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        f"-dPDFSETTINGS={level}",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_pdf_path}",
        input_pdf_path,
    ]

    try:
        subprocess.run(gs_command, check=True)
    except FileNotFoundError:
        print("Ghostscript not found. Check the installation path!")
        break
    except subprocess.CalledProcessError:
        print("Ghostscript failed to compress the file.")
        break

    if not os.path.exists(output_pdf_path):
        print("Output file was not created. Check file paths and permissions.")
        break

    file_size_bytes = os.path.getsize(output_pdf_path)
    file_size_mb = file_size_bytes / (1024 * 1024)

    print(f"📏 Current size: {file_size_mb:.2f} MB")

    if file_size_bytes <= max_size_bytes:
        print(f"✅ Successfully compressed under {max_size_mb} MB!")
        break

print(f"Final compressed file: {output_pdf_path}")
