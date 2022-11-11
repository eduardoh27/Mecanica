import matplotlib.pyplot as plt
import numpy as np

def main1():
    
    #plt.style.use(['science','no-latex'])
    

    v_0 = 5
    w = 5

    t = np.linspace(0, 5, 1000)

    theta = lambda t :  w*t
    r = lambda t: v_0*t
       
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta(t), r(t))

    ax.set_rmax(5)
    #ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
    #ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
    ax.grid(True)

    ax.set_title("Carro en plataforma giratoria", va='bottom')
    plt.savefig('tarea2carroGirando.png', dpi=300, bbox_inches='tight')
    plt.show()

def main2():
    None
 
if __name__ == "__main__":
    main1()
