import os
import matplotlib.pyplot as plt

def plot_data(data):
    plt.plot(data)
    plt.show()

class Plot:
    def __init__(self, data):
        self.data = data

    def plot_data(self):
        plt.plot(self.data)
        plt.show()
    
    def save_plot(self, filename):
        plt.plot(self.data)
    
    def coxx_plot(self, output_fol, data_name, data, label):
        """
        COHP, COOP, COBI plot for the data

        Parameters:
            output_fol (str): Folder to save the plot
            data_name (str): Name of the data
            data (DataFrame): Data to plot (Energy, COXX)
            label (str): Label for the plot ex: COHP, COOP, COBI
        """
        if output_fol is None:
            os.mkdir(output_fol)

        if data.ndim != 2 or data.shape[1] < 2:
            raise ValueError("data must be a 2D array with at least two columns")
        elif data.shape[1] > 3:
            raise ValueError("The data has too much columns")

        fig, ax = plt.subplots(1, 1, figsize=(3, 5))
        fig.subplots_adjust(bottom=0.15)
        fig.subplots_adjust(left=0.25)
        ax.plot(data.iloc[:, 1], data.iloc[:, 0], label=label)
        ax.set_xlabel(label, fontsize=15)
        ax.set_ylabel('Energy (eV)', fontsize=15)
        ax.tick_params(axis='both', which='major', labelsize=12)
        ax.set_title(f'{label} vs Energy')
        ax.legend()
        plt.savefig(f'{output_fol}/{data_name}_{label}.png')
        plt.close()