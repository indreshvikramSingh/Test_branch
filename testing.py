


# import tkinter as tk
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# from numpy import nan
# from matplotlib.ticker import MaxNLocator

# class ZoomPan:
#     def __init__(self, ax, canvas):
#         self.ax = ax
#         self.canvas = canvas
#         self.canvas.mpl_connect('scroll_event', self.zoom)

#     def zoom(self, event):
#         base_scale = 1.2
#         cur_xlim = self.ax.get_xlim()
#         cur_ylim = self.ax.get_ylim()

#         xdata = event.xdata
#         ydata = event.ydata
#         if xdata is None or ydata is None:
#             return
        
#         if event.button == 'up':
#             scale_factor = 1 / base_scale
#         elif event.button == 'down':
#             scale_factor = base_scale
#         else:
#             scale_factor = 1
        
#         new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
#         new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor
    
#         relx = (cur_xlim[1] - xdata) / (cur_xlim[1] - cur_xlim[0])
#         rely = (cur_ylim[1] - ydata) / (cur_ylim[1] - cur_ylim[0])
    
#         self.ax.set_xlim([xdata - new_width * (1 - relx), xdata + new_width * (relx)])
#         self.ax.set_ylim([ydata - new_height * (1 - rely), ydata + new_height * (rely)])
#         self.canvas.draw()

# def plot_graph():
#     file_path = path_var.get()
#     if not file_path:
#         return

#     try:
#         df = pd.read_csv(file_path, header=None)

#         #  Subsampling step to improve readability
#         sampling_step = 10 
#         time = df[0][::sampling_step].reset_index(drop=True)
#         breath = df[5][::sampling_step].reset_index(drop=True)

#         for widget in graph_frame.winfo_children():
#             widget.destroy()

#         apnea_events = []
#         current_event = []
#         for i in range(len(breath)):
#             if breath[i] <= 2:
#                 current_event.append(i)
#             else:
#                 if len(current_event) >= 3:
#                     apnea_events.append(current_event)
#                 current_event = []
#         if len(current_event) >= 3:
#             apnea_events.append(current_event)

#         classified_events = []
#         for event in apnea_events:
#             start = event[0]
#             end = event[-1]
#             after_end = breath[end + 1] if end + 1 < len(breath) else 0
#             if after_end > 5:
#                 classified_events.append((start, end, 'OSA'))
#             elif after_end <= 2:
#                 classified_events.append((start, end, 'CSA'))
#             else:
#                 classified_events.append((start, end, 'MSA'))

#         fig, ax = plt.subplots(figsize=(14, 6), dpi=100)
#         fig.patch.set_facecolor('white')
#         ax.set_facecolor('white')

#         last_end = 0
#         for start, end, event_type in classified_events:
#             if start > last_end:
#                 x = list(time[last_end:start]) + [nan]
#                 y = list(breath[last_end:start]) + [nan]
#                 ax.plot(x, y, color='green', linewidth=0.3) 

#             color = {'OSA': 'red', 'CSA': 'blue', 'MSA': 'orange'}[event_type]
#             x = list(time[start:end+1]) + [nan]
#             y = list(breath[start:end+1]) + [nan]
#             ax.plot(x, y, color=color, linewidth=2)
#             last_end = end + 2

#         if last_end < len(time):
#             x = list(time[last_end:]) + [nan]
#             y = list(breath[last_end:]) + [nan]
#             ax.plot(x, y, color='green', linewidth=0.3)

#         osa_count = sum(1 for _, _, t in classified_events if t == 'OSA')
#         csa_count = sum(1 for _, _, t in classified_events if t == 'CSA')
#         msa_count = sum(1 for _, _, t in classified_events if t == 'MSA')

#         ax.set_title(f"OSA: {osa_count}   CSA: {csa_count}   MSA: {msa_count}", fontsize=13)
#         ax.set_xlabel("Time")
#         ax.set_ylabel("Breath Value")
#         ax.grid(True, alpha=0.2)

#         for label in ax.get_xticklabels():
#             label.set_rotation(45)
#             label.set_fontsize(8)

#         for label in ax.get_yticklabels():
#             label.set_fontsize(8)

#         ax.xaxis.set_major_locator(MaxNLocator(nbins=15))
#         fig.tight_layout()

#         canvas = FigureCanvasTkAgg(fig, master=graph_frame)
#         canvas.draw()

#         toolbar = NavigationToolbar2Tk(canvas, graph_frame)
#         toolbar.update()
#         toolbar.pack(side=tk.TOP, fill=tk.X)

#         canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

#         ZoomPan(ax, canvas)

#     except Exception as e:
#         print(f"Error: {e}")

# # GUI
# root = tk.Tk()
# root.title("Breath Trend Viewer")
# root.geometry("1100x650")

# path_var = tk.StringVar(root, value="C:\\Users\\Deckmount\\Documents\\DATA0637.csv")

# tk.Label(root, text="CSV File Path:", font=("Arial", 12)).pack(pady=5)
# tk.Entry(root, textvariable=path_var, width=70, font=("Arial", 11)).pack(pady=5)
# tk.Button(root, text="Plot Graph", command=plot_graph, font=("Arial", 11)).pack(pady=5)

# graph_frame = tk.Frame(root)
# graph_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# root.mainloop()






















# import tkinter as tk
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# from numpy import nan
# from matplotlib.ticker import MaxNLocator







# def plot_graph():
#     file_path = path_var.get()
#     if not file_path:
#         return

#     try:
#         df = pd.read_csv(file_path, header=None)
#         time = df[0]
#         breath = df[5]

#         for widget in graph_frame.winfo_children():
#             widget.destroy()

#         apnea_events = []
#         current_event = []
#         for i in range(len(breath)):
#             if breath[i] <= 2:
#                 current_event.append(i)
#             else:
#                 if len(current_event) >= 3:
#                     apnea_events.append(current_event)
#                 current_event = []
#         if len(current_event) >= 3:
#             apnea_events.append(current_event)

#         classified_events = []
#         for event in apnea_events:
#             start = event[0]
#             end = event[-1]
#             after_end = breath[end + 1] if end + 1 < len(breath) else 0
#             if after_end > 5:
#                 classified_events.append((start, end, 'OSA'))
#             elif after_end <= 2:
#                 classified_events.append((start, end, 'CSA'))
#             else:
#                 classified_events.append((start, end, 'MSA'))

#         fig, ax = plt.subplots(figsize=(18, 6), dpi=100)
#         fig.patch.set_facecolor('white')
#         ax.set_facecolor('white')

#         sampling_step = 20
#         last_end = 0
#         for start, end, event_type in classified_events:
#             if start > last_end:
#                 x = list(time[last_end:start:sampling_step]) + [nan]
#                 y = list(breath[last_end:start:sampling_step]) + [nan]
#                 ax.plot(x, y, color='purple', linewidth=0.6, alpha=0.5)

#             color = {'OSA': 'red', 'CSA': 'blue', 'MSA': 'orange'}[event_type]
#             x = list(time[start:end+1:sampling_step]) + [nan]
#             y = list(breath[start:end+1:sampling_step]) + [nan]
#             ax.plot(x, y, color=color, linewidth=1.2, alpha=0.9)
#             last_end = end + 2

#         if last_end < len(time):
#             x = list(time[last_end::sampling_step]) + [nan]
#             y = list(breath[last_end::sampling_step]) + [nan]
#             ax.plot(x, y, color='purple', linewidth=0.6, alpha=0.5)

#         osa_count = sum(1 for _, _, t in classified_events if t == 'OSA')
#         csa_count = sum(1 for _, _, t in classified_events if t == 'CSA')
#         msa_count = sum(1 for _, _, t in classified_events if t == 'MSA')

#         ax.set_title(f"OSA: {osa_count}   CSA: {csa_count}   MSA: {msa_count}", fontsize=14, fontweight='bold')
#         ax.set_xlabel("Time", fontsize=12)
#         ax.set_ylabel("Breath Value", fontsize=12)
#         ax.grid(True, alpha=0.2)

#         for label in ax.get_xticklabels():
#             label.set_rotation(45)
#             label.set_fontsize(8)
#         for label in ax.get_yticklabels():
#             label.set_fontsize(8)
#         ax.xaxis.set_major_locator(MaxNLocator(nbins=15))
#         fig.tight_layout()

#         canvas = FigureCanvasTkAgg(fig, master=graph_frame)
#         canvas.draw()
#         toolbar = NavigationToolbar2Tk(canvas, graph_frame)
#         toolbar.update()
#         toolbar.pack(side=tk.TOP, fill=tk.X)
#         canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        

#     except Exception as e:
#         print(f"Error: {e}")

# # GUI
# root = tk.Tk()
# root.title("Breath Trend Viewer")
# root.geometry("1200x700")

# path_var = tk.StringVar(root, value="C:\\Users\\Deckmount\\Documents\\DATA0637.csv")

# tk.Label(root, text="CSV File Path:", font=("Arial", 12)).pack(pady=5)
# tk.Entry(root, textvariable=path_var, width=70, font=("Arial", 11)).pack(pady=5)
# tk.Button(root, text="Plot Graph", command=plot_graph, font=("Arial", 11)).pack(pady=5)

# graph_frame = tk.Frame(root)
# graph_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# root.mainloop()











import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from numpy import nan
from matplotlib.ticker import MaxNLocator

class ZoomPan:
    def __init__(self, ax, canvas):
        self.ax = ax
        self.canvas = canvas
        self.press = None
        self.canvas.mpl_connect("scroll_event", self.zoom)

    def zoom(self, event):
        base_scale = 1.2
        cur_xlim = self.ax.get_xlim()
        cur_ylim = self.ax.get_ylim()

        xdata = event.xdata
        ydata = event.ydata
        if xdata is None or ydata is None:
            return

        if event.button == 'up':
            scale_factor = 1 / base_scale
        elif event.button == 'down':
            scale_factor = base_scale
        else:
            scale_factor = 1

        new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
        new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

        relx = (cur_xlim[1] - xdata) / (cur_xlim[1] - cur_xlim[0])
        rely = (cur_ylim[1] - ydata) / (cur_ylim[1] - cur_ylim[0])

        self.ax.set_xlim([xdata - new_width * (1 - relx), xdata + new_width * relx])
        self.ax.set_ylim([ydata - new_height * (1 - rely), ydata + new_height * rely])
        self.canvas.draw()

def plot_graph():
    file_path = path_var.get()
    if not file_path:
        return

    try:
        df = pd.read_csv(file_path, header=None)
        time = df[0]
        breath = df[5]

        for widget in graph_frame.winfo_children():
            widget.destroy()

        apnea_events = []
        current_event = []
        for i in range(len(breath)):
            if breath[i] <= 2:
                current_event.append(i)
            else:
                if len(current_event) >= 3:
                    apnea_events.append(current_event)
                current_event = []
        if len(current_event) >= 3:
            apnea_events.append(current_event)

        classified_events = []
        for event in apnea_events:
            start = event[0]
            end = event[-1]
            after_end = breath[end + 1] if end + 1 < len(breath) else 0
            if after_end > 5:
                classified_events.append((start, end, 'OSA'))
            elif after_end <= 2:
                classified_events.append((start, end, 'CSA'))
            else:
                classified_events.append((start, end, 'MSA'))

        fig, ax = plt.subplots(figsize=(18, 6), dpi=100)
        fig.patch.set_facecolor('white')
        ax.set_facecolor('white')

        sampling_step = 20
        last_end = 0
        for start, end, event_type in classified_events:
            if start > last_end:
                x = list(time[last_end:start:sampling_step]) + [nan]
                y = list(breath[last_end:start:sampling_step]) + [nan]
                ax.plot(x, y, color='purple', linewidth=0.6, alpha=0.5)

            color = {'OSA': 'red', 'CSA': 'blue', 'MSA': 'orange'}[event_type]
            x = list(time[start:end+1:sampling_step]) + [nan]
            y = list(breath[start:end+1:sampling_step]) + [nan]
            ax.plot(x, y, color=color, linewidth=1.2, alpha=0.9)
            last_end = end + 2

        if last_end < len(time):
            x = list(time[last_end::sampling_step]) + [nan]
            y = list(breath[last_end::sampling_step]) + [nan]
            ax.plot(x, y, color='purple', linewidth=0.6, alpha=0.5)

        osa_count = sum(1 for _, _, t in classified_events if t == 'OSA')
        csa_count = sum(1 for _, _, t in classified_events if t == 'CSA')
        msa_count = sum(1 for _, _, t in classified_events if t == 'MSA')

        ax.set_title(f"OSA: {osa_count}   CSA: {csa_count}   MSA: {msa_count}", fontsize=14, fontweight='bold')
        ax.set_xlabel("Time", fontsize=12)
        ax.set_ylabel("Breath Value", fontsize=12)
        ax.grid(True, alpha=0.2)

        for label in ax.get_xticklabels():
            label.set_rotation(45)
            label.set_fontsize(8)
        for label in ax.get_yticklabels():
            label.set_fontsize(8)
        ax.xaxis.set_major_locator(MaxNLocator(nbins=15))
        fig.tight_layout()

        # Add colored horizontal lines as legend without text
        y_min, y_max = ax.get_ylim()
        legend_y = y_max + (y_max - y_min) * 0.05  # Position above plot
        ax.hlines(legend_y, time.iloc[0], time.iloc[0] + 20, colors='red', linewidth=5)
        ax.hlines(legend_y, time.iloc[0] + 25, time.iloc[0] + 45, colors='blue', linewidth=5)
        ax.hlines(legend_y, time.iloc[0] + 50, time.iloc[0] + 70, colors='orange', linewidth=5)
        ax.set_ylim(y_min, legend_y + (y_max - y_min) * 0.1)  # Adjust y-limits to fit legend lines

        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, graph_frame)
        toolbar.update()
        toolbar.pack(side=tk.TOP, fill=tk.X)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        ZoomPan(ax, canvas)

    except Exception as e:
        print(f"Error: {e}")

# GUI
root = tk.Tk()
root.title("Breath Trend Viewer")
root.geometry("1200x700")

path_var = tk.StringVar(root, value="C:\\Users\\Deckmount\\Documents\\DATA0637.csv")

tk.Label(root, text="CSV File Path:", font=("Arial", 12)).pack(pady=5)
tk.Entry(root, textvariable=path_var, width=70, font=("Arial", 11)).pack(pady=5)
tk.Button(root, text="Plot Graph", command=plot_graph, font=("Arial", 11)).pack(pady=5)

graph_frame = tk.Frame(root)
graph_frame.pack(fill=tk.BOTH, expand=True, pady=10)

root.mainloop()
