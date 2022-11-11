import matplotlib.pyplot as plt
import numpy as np

def main():

    plt.style.use(['science','no-latex'])
    
    l = 1
    m1 = 2
    m2 = 2
    g = 9.8

    I = 1
    R = 1

    py1_ideal = lambda y : np.sqrt( (2*(m1+m2)) * ((y*g*(m1-m2))+((g*l/2)*(m2-m1))) )
    py1_polea = lambda y : np.sqrt( (2*(m1+m2+ (I/(R**2)))) * ((y*g*(m1-m2))+((g*(l+np.pi*R)/2)*(m2-m1))) )


    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_title('Espacio de fase (m1>m2)')
    ax.set_xlabel('y',fontsize=10)
    ax.set_ylabel('Py',fontsize=10)
    
    valores_y = np.linspace(0, 10, int(1e6))
    
    plt.plot(valores_y, py1_ideal(valores_y), label = 'polea ideal')
    plt.plot(valores_y, py1_polea(valores_y), label = 'polea de masa Mp')
        
    #ax.legend(loc ="upper left")
    
    plt.savefig('tarea4grafica3.png', dpi=300, bbox_inches='tight')
    plt.show()
 
if __name__ == "__main__":
    main()
    