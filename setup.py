import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
import os

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mesclador de PDFs CTI GRE11")
        self.center_window(800, 700)
        

        # Lista para armazenar os arquivos selecionados
        self.files = []

        # Interface
        self.label = tk.Label(root, text="Selecione arquivos PDF para mesclar:")
        self.label.pack(pady=10)

        self.add_button = tk.Button(root, text="Adicionar PDFs", command=self.add_files, font=("Arial", 12, "bold"))
        self.add_button.pack(pady=5)

        self.listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=25)
        self.listbox.pack(pady=10)

        self.merge_button = tk.Button(root, text="Mesclar PDFs", command=self.merge_pdfs, font=("Arial", 12, "bold"))
        self.merge_button.pack(pady=10)

        self.clear_button = tk.Button(root, text="Limpar Lista", command=self.clear_list, font=("Arial", 12, "bold"))
        self.clear_button.pack(pady=5)

    def center_window(self, width, height):
        """Centraliza a janela na tela."""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def add_files(self):
        # Abre diálogo para seleção de arquivos PDF
        new_files = filedialog.askopenfilenames(filetypes=[("Arquivos PDF", "*.pdf")])
        if new_files:
            # Adiciona arquivos na lista e na interface
            self.files.extend(new_files)
            for file in new_files:
                self.listbox.insert(tk.END, file)

    def clear_list(self):
        # Limpa a lista
        self.files.clear()
        self.listbox.delete(0, tk.END)

    def merge_pdfs(self):
        if len(self.files) < 2:
            messagebox.showwarning("Aviso", "Selecione pelo menos dois arquivos para mesclar.")
            return

        # Pede ao usuário para selecionar o local para salvar o arquivo mesclado
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Arquivos PDF", "*.pdf")])
        if not save_path:
            return

        try:
            # Mescla os arquivos
            merger = PdfMerger()
            for pdf in self.files:
                merger.append(pdf)

            merger.write(save_path)
            merger.close()

            messagebox.showinfo("Sucesso", f"PDFs mesclados salvos em: {save_path}")
            self.clear_list()

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao mesclar os PDFs: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
