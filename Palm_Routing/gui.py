from generator import personal_df,professional_df,project_df,certification_df,education_df,area_df,technical_df,interpersonal_df
import tkinter as tk
from tkinter import ttk


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        # Create a vertical scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Create a canvas to contain the frame's contents
        canvas = tk.Canvas(self, yscrollcommand=scrollbar.set)
        canvas.grid(row=0, column=0, sticky="nsew")

        # Attach the scrollbar to the canvas
        scrollbar.config(command=canvas.yview)

        # Create a frame to hold the contents of the canvas
        self.scrollable_frame = ttk.Frame(canvas)
        self.scrollable_frame.grid(row=0, column=0, sticky="nsew")

        # Add the frame to the canvas
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Configure row and column weights for resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Bind the canvas resizing to the frame size
        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
class ResumeEditorApp:
    def __init__(self, root, df):
        self.root = root
        self.root.title("Resume Editor")

        # Store original personal_df
        self.original_df = df.copy()
        updated_df=df.copy()

        self.current_row_index = 0

        # Create a frame for the content
        self.content_frame = ttk.Frame(scrollable_frame.scrollable_frame,borderwidth=2)
        self.content_frame.pack(fill='both', expand=True)

        # Create labels and entry widgets for each column of personal_df
        self.create_widgets_for_personal_dataframe(df)

        # Add a Save button for personal_df
        save_button_personal = ttk.Button(self.content_frame, text="Save Changes", command=self.save_changes_personal,style='Green.TButton')
        save_button_personal.grid(row=self.current_row_index, columnspan=len(df.columns) * 2, pady=10)
        ttk.Separator(scrollable_frame.scrollable_frame, orient=tk.HORIZONTAL).pack(fill="x", pady=5)

    def create_widgets_for_personal_dataframe(self, df):
        # Increase the width and height of the widgets
        label_width = 20
        entry_width = 20
        font_size = 9

        # Create labels for each column
        for col_index, col_name in enumerate(df.columns):
            col_label = tk.Label(self.content_frame, text=col_name, width=label_width)
            col_label.grid(row=self.current_row_index, column=col_index * 2, padx=5, pady=5, sticky=tk.E)

            # Create entry widgets for each record in the column
            for row_index, value in enumerate(df[col_name]):
                entry = tk.Entry(self.content_frame, width=entry_width, font=("Arial", font_size))
                entry.insert(tk.END, str(value))  # Convert to string in case of numeric values
                entry.grid(row=row_index + 1, column=col_index * 2 + 1, padx=5, pady=5)

        # Update the current row index for the next DataFrame
        self.current_row_index += len(df) + 2

    def save_changes_personal(self):
        # Update the original personal_df with the edited values
        df = self.original_df

        for col_index, col_name in enumerate(df.columns):
            updated_values = [entry.get() for entry in self.content_frame.children.values() if isinstance(entry, tk.Entry) and entry.grid_info()['column'] == col_index * 2 + 1]

            # Check if the length of updated values matches the length of the original dataframe
            if len(updated_values) == len(df):
                df[col_name] = updated_values
            else:
                print(f"Length mismatch for {col_name} in personal_df. Expected {len(df)} values, got {len(updated_values)}.")

        # You can print or store the updated dataframe as needed
        self.original_df=df
        print("Updated dataframe:")
        print(df)
    def get_updated_df(self):
        return self.original_df


root = tk.Tk()
style = ttk.Style()
style.configure('Green.TButton', background='black', foreground='green')
scrollable_frame = ScrollableFrame(root)
scrollable_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
app = ResumeEditorApp(root, personal_df)
updated_personal_df=app.get_updated_df()
app1 = ResumeEditorApp(root, education_df)
updated_education_df=app1.get_updated_df()
app2 = ResumeEditorApp(root, area_df)
updated_area_df=app2.get_updated_df()
app3 = ResumeEditorApp(root, technical_df)
updated_technical_df=app3.get_updated_df()
app4 = ResumeEditorApp(root, interpersonal_df)
updated_interpersonal_df=app4.get_updated_df()
app5 = ResumeEditorApp(root, certification_df)
updated_certification_df=app5.get_updated_df()
app6 = ResumeEditorApp(root, project_df)
updated_project_df=app6.get_updated_df()
app7 = ResumeEditorApp(root, professional_df)
updated_professional_df=app7.get_updated_df()
root.mainloop()
