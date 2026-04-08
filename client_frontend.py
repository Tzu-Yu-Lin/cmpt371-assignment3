import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox
from client_backend import CBackend

HOST = "127.0.0.1"
PORT = 8888


class ChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat GUI Client")
        self.root.geometry("600x450")

        self.backend = None
        self.username = ""

        self.build_gui()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def build_gui(self):
        self.status_label = tk.Label(self.root, text="Not connected")
        self.status_label.pack()

        self.chat_area = scrolledtext.ScrolledText(self.root, state="disabled")
        self.chat_area.pack(fill="both", expand=True, padx=10, pady=5)

        frame = tk.Frame(self.root)
        frame.pack(fill="x", padx=10, pady=10)

        self.entry = tk.Entry(frame)
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", self.send_message)

        tk.Button(frame, text="Send", command=self.send_message).pack(side="right")
        tk.Button(self.root, text="Connect", command=self.connect).pack(pady=5)

    def connect(self):
        if self.backend:
            return

        username = simpledialog.askstring("Username", "Enter username:")
        if not username:
            return

        self.username = username

        self.backend = CBackend(
            HOST,
            PORT,
            self.on_message,
            self.on_disconnect
        )

        try:
            self.backend.join(username)
            self.status_label.config(text=f"Connected as {username}")
            self.append("[SYSTEM] Connected to server")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.backend = None

    def send_message(self, event=None):
        if not self.backend:
            return

        text = self.entry.get().strip()
        if not text:
            return

        self.backend.send(f"{self.username}: {text}")
        self.entry.delete(0, tk.END)

    def on_message(self, message):
        self.append(message)

    def on_disconnect(self):
        self.append("[SYSTEM] Disconnected")
        self.status_label.config(text="Not connected")
        self.backend = None

    def append(self, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.yview(tk.END)
        self.chat_area.config(state="disabled")

    def on_close(self):
        if self.backend:
            self.backend.close()
        self.root.destroy()


def main():
    root = tk.Tk()
    app = ChatGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()