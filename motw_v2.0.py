import subprocess
import os
import tempfile
import shutil

SOURCE = r"C:\path\to\scanned"

def unblock_file(path):
    """Remove Mark of the Web (Zone.Identifier) from a file."""
    subprocess.run(
        ["powershell", "-Command", f"Unblock-File -Path '{path}'"],
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

for root, dirs, files in os.walk(SOURCE):
    for file in files:
        if file.lower().endswith(".pdf"):
            src_file = os.path.join(root, file)

            # Remove MOTW before repairing
            unblock_file(src_file)

            # Create a temporary file in the same directory
            with tempfile.NamedTemporaryFile(dir=root, delete=False) as tmp:
                tmp_path = tmp.name

            # Run qpdf to "repair" the PDF into the temp file
            result = subprocess.run(
                ["qpdf", "--linearize", src_file, tmp_path],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                # Replace the original file with the repaired one
                shutil.move(tmp_path, src_file)
                print(f"✅ Repaired and unblocked: {src_file}")
            else:
                print(f"❌ Failed to repair {src_file}: {result.stderr}")
                os.remove(tmp_path)
