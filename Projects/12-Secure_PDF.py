from PyPDF2 import PdfReader, PdfWriter

# this one copies and creates new file
reader = PdfReader("Projects/Assets/file.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt("protect_password")

# add this
with open("Projects/Assets/protected_file.pdf", "wb") as f:
    writer.write(f)


