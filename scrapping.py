import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from PIL import Image, ImageTk
from io import BytesIO
import re
from urllib.parse import urljoin

class WebScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraper")
        self.root.geometry("800x600")

        style = ttk.Style()
        style.theme_use("clam")

        self.create_widgets()

    def create_widgets(self):
        self.label_instruction = ttk.Label(self.root, text="Digite a URL do site:")
        self.label_instruction.pack(pady=10)

        self.entry_url = ttk.Entry(self.root, width=60)
        self.entry_url.pack(pady=10)

        self.btn_obter_informacoes = ttk.Button(self.root, text="Obter Informações", command=self.obter_informacoes)
        self.btn_obter_informacoes.pack(pady=10)

        self.btn_limpar = ttk.Button(self.root, text="Limpar", command=self.limpar_campos)
        self.btn_limpar.pack(pady=10)

        self.label_resultado = ttk.Label(self.root, text="Resultado:")
        self.label_resultado.pack(pady=10)

        self.text_resultado = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=20)
        self.text_resultado.pack(pady=10)

        self.historico = []

    def obter_informacoes(self):
        url = self.entry_url.get()
        if self.validar_url(url):
            resultado, dados_multimidia, texto = self.extrair_dados_multimidia(url)
            self.exibir_resultado(resultado, dados_multimidia, texto)
            self.historico.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {url}")

    def validar_url(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return True
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro de requisição: {e}")
            return False

    def extrair_dados_multimidia(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            print("Tentando extrair URLs das imagens...")
            urls_imagens = self.extrair_elementos(soup, "img", atributos=["src", "data-src"])
            print("URLs das imagens extraídas:", urls_imagens)

            print("Tentando extrair URLs dos vídeos...")
            urls_videos = self.extrair_urls_videos(soup)
            print("URLs dos vídeos extraídos:", urls_videos)

            print("Tentando extrair texto do conteúdo principal...")
            texto = self.extrair_texto(soup)
            print("Texto do conteúdo principal extraído:", texto)

            return "", {"urls_imagens": urls_imagens, "urls_videos": urls_videos}, texto

        except Exception as e:
            return f"Erro: {e}", {}, ""

    def extrair_elementos(self, soup, tag, atributos=None):
        elementos = soup.find_all(tag)
        urls = []
        for elemento in elementos:
            for atributo in atributos:
                url = elemento.get(atributo)
                if url:
                    urls.append(url)
                    break
        return urls

    def extrair_urls_videos(self, soup):
        urls_videos = []
        iframes = soup.find_all("iframe", {"src": re.compile(r'https://www\.youtube\.com/embed/')})
        for iframe in iframes:
            urls_videos.append(iframe["src"])
        return urls_videos

    def extrair_texto(self, soup):
        texto = soup.get_text(separator='\n', strip=True)
        return texto

    def exibir_resultado(self, resultado, dados_multimidia, texto):
        self.label_resultado.config(text="Resultado:")
        self.text_resultado.delete(1.0, tk.END)
        self.text_resultado.insert(tk.END, resultado)

        if "urls_imagens" in dados_multimidia:
            for i, url_imagem in enumerate(dados_multimidia["urls_imagens"]):
                imagem = self.baixar_imagem(url_imagem)
                if imagem:
                    self.exibir_imagem(imagem, f"Imagem_{i + 1}")

        if "urls_videos" in dados_multimidia:
            for i, url_video in enumerate(dados_multimidia["urls_videos"]):
                self.baixar_video(url_video, f"Video_{i + 1}.mp4")

        if texto:
            self.salvar_texto(texto, "Texto_Principal.txt")

    def baixar_imagem(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            imagem = Image.open(BytesIO(response.content))
            return imagem
        except Exception as e:
            print(f"Erro ao baixar imagem: {e}")
            return None

    def exibir_imagem(self, imagem, titulo):
        imagem.thumbnail((100, 100))
        imagem_tk = ImageTk.PhotoImage(imagem)
        self.text_resultado.image_create(tk.END, image=imagem_tk)
        self.text_resultado.insert(tk.END, f"\n{titulo}\n")

    def baixar_video(self, url, nome_arquivo):
        try:
            response = requests.get(url)
            response.raise_for_status()
            with open(nome_arquivo, 'wb') as file:
                file.write(response.content)
        except Exception as e:
            print(f"Erro ao baixar vídeo: {e}")

    def salvar_texto(self, texto, nome_arquivo):
        try:
            with open(nome_arquivo, 'w', encoding='utf-8') as file:
                file.write(texto)
        except Exception as e:
            print(f"Erro ao salvar texto: {e}")

    def limpar_campos(self):
        self.entry_url.delete(0, tk.END)
        self.label_resultado.config(text="Resultado:")
        self.text_resultado.delete(1.0, tk.END)
        self.root.bell()

if __name__ == "__main__":
    root = tk.Tk()
    app = WebScraperApp(root)
    root.mainloop()
