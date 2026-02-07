from weasyprint import HTML

HTML("output/recibo.html").write_pdf("output/recibo.pdf")

print("PDF generado correctamente")
