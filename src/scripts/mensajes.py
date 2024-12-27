

def mensaje_graficoGasto_cliente(cluster):
  if(cluster==0):
    print('''Los porcentajes indican qué fracción del gasto total en cada grupo es atribuible a los diferentes géneros.
El gráfico sugiere que, en todos los grupos de ingresos, los hombres tienen una participación significativamente mayor en el
gasto total, especialmente en los grupos de ingresos bajos, medios e indeterminados. Las mujeres tienen una menor participación
en todos los grupos de ingresos, mientras que el género indeterminado contribuye con el menor porcentaje en general.
Dado que los hombres representan la mayor parte del gasto en todos los grupos de ingresos, especialmente en los segmentos de
ingresos bajos, medios e indeterminados, las campañas de marketing podrían orientarse más hacia este público.
Ofrecer productos y promociones que se alineen con las preferencias de este grupo sería una estrategia clave, ya que tienen
una mayor propensión a gastar.
Un enfoque de personalización en el sitio web, mostrando diferentes productos o promociones en función del género del cliente
(si se dispone de esta información), podría mejorar la experiencia del usuario y potencialmente aumentar las conversiones de las mujeres.
El porcentaje de gasto del género indeterminado es bajo en comparación con los hombres y mujeres en todos los grupos
de ingresos. Esto podría indicar que el sitio web no está siendo lo suficientemente inclusivo o atractivo para este grupo.
Se podría considerar realizar mejoras en la usabilidad del sitio, asegurándose de que sea inclusivo para personas de todos
los géneros, lo que podría incluir ajustes en el lenguaje, las opciones de género en los formularios de registro o la
representación de productos y modelos diversos.
Estrategias como opciones de financiamiento, descuentos por volumen, o promociones de productos esenciales podrían resonar
mejor con estos segmentos, maximizando el valor por cliente en estos grupos.
Ofertas como ventas flash, recomendaciones de productos relacionadas, y envíos rápidos o gratuitos podrían aumentar las conversiones y los ingresos.
Dado que los hombres son los principales consumidores en todos los grupos, un programa de fidelización dirigido a ellos
podría ser muy efectivo. Esto podría incluir recompensas por compras frecuentes, descuentos personalizados o membresías
exclusivas para mantener a estos consumidores comprometidos con la plataforma.
Las ofertas pueden incluir productos exclusivos, tecnologías de punta, artículos de lujo, y envíos rápidos o gratuitos.
En lugar de campañas exclusivas para hombres o mujeres, se pueden crear campañas neutras de género que apelen a una audiencia
más amplia y diversa.''')
  elif(cluster==1):
    print('''''')



def mensaje_grafico_Edades_pais(cluster):
  if(cluster==0):

    print('''Se observa una alta representatividad de la categoría "Joven", en todos los países. Siendo en Alemania,
Reino Unido, Estados Unidos y Australia una significativa proporción de los clientes que se encuentran en estos países.
Las estrategias de marketing y ofertas para estos países deberían incluir productos orientados a consumidores jóvenes.
Entre estos podría considerarse productos de tecnología, ropa de moda y otros; más adelante en el análisis se estudiará los productos más comprados por este grupo.
Canadá y Australia tienen una distribución más balanceada entre las categorías "Joven", "Adulto Joven" y "Adulto", lo que indica que las campañas en estos países .
Algunos países, como Alemania, Canadá y Australia, tienen una notable proporción de "Adulto Joven" y "Adulto".
Las estrategias de marketing deben diversificarse para diferentes segmentos etarios. Considerar productos que productos sean de interés para clientes jóvenes como también productos dirigidos a personas de más edad.
Algunos ejemplos podrían ser, electrodomésticos, productos de salud y bienestar, entre otros.
          ''')



def mensaje_grafico_gastos_genero_edad(cluster):
  if(cluster==0):
    print('''Como se puede apreciar en el gráfico, la distribución de gasto en los jóvenes es muy parecida, tanto para mujeres como hombres.
En el caso de Adulto-Joven, las mujeres gastan un poco más que los hombres.
En los adultos, adultos mayores y veteranos, los hombres gastan más.
El grupo de género indeterminado se encuentra con una distribución menos dispersa, no presenta casi datos atípicos y en general gastan lo mismo o en el caso de los adultos y veteranos, más que los otros
géneros. Se recomienda replantear la descripción de género para ser más inclusivo con el grupo y aplicar publicidades destinadas a aumentar la participación de personas de este grupo.''')



def mensaje_grafico_gastos_genero_ingreso(cluster):
  if(cluster==0):
    print('''En el caso de la distribucion del gasto por genero y grupo de ingresos, se observa que las personas que pertenecen al
genero Femenino y el grupo de ingresos altos, tienden a gastar mas que los hombres y personas del genero indeterminado.
Teniendo en cuenta el grafico anterior, podria ser beneficioso realizar campañas de marketing apuntadas a ofrecer
productos premium, a personas dentro de estas categorias.
    ''')


def mensaje_grafico_productos_mas_comprados(cluster):
  if(cluster==0):
    print('''Las categorías de Food y Clothing son las más compradas en todos los grupos de ingresos. Lo que hace que sea crucial prestar atención al stock de estos productos para garantizar su disponibilidad.
También se destaca la categoría de Books, en todos los segmentos de mercado.

Una estrategia efectiva podría ser ofrecer devoluciones en la categoría de ropa, permitiendo a los clientes seleccionar
lo que les gusta, probarse las prendas y devolver lo que no les interesa. Además, se podría fomentar el alquiler y la compra de libros, optimizando los envíos de ambas categorías y ofreciendo envío
gratuito a los clientes que realicen devoluciones y alquilen o compren libros.

El grupo de ingresos bajos muestra interés por productos de decoración para el hogar. Ofrecer artículos decorativos que complementen la comida podría potenciar las ventas,
como bandejas decorativas, platos y jarras.

Las categorías de tecnología, como smartphones y televisores, están presentes en todos los grupos. Dado que estos productos suelen tener precios más elevados, sería beneficioso explorar
estrategias para impulsar las ventas en estas categorías. En particular, los teléfonos móviles, que requieren poco espacio de almacenamiento y son fáciles de transportar, podrían beneficiarse
de opciones de financiamiento. También se podría considerar la inclusión de suscripciones a plataformas de streaming, audiolibros o juegos para incentivar la compra.

Finalmente, es recomendable evaluar la categoría de Sports, ya sea eliminándola o investigando más a fondo su baja popularidad.''')



def mensaje_grafico_dispersion_gastos_frecuencia(cluster):

  if(cluster==0):
    print('''El gráfico muestra una clara correlación positiva entre la cantidad total comprada y el gasto histórico del cliente. Ademas muestra como el tamaño de los circulos aumentan conforme aumenta la frecuencia de compra.
A medida que aumenta el TotalHistorico_CompradoCliente, también lo hace el TotalHistorico_GastadoCliente y con ello la frecuencia de compra. Esto sugiere que los clientes que compran más también tienden a gastar más.
Los clientes que realizan compras más frecuentes o de mayor volumen también representan un mayor valor para el negocio en términos de ingresos.
Aunque la correlación es positiva, hay una dispersión significativa entre los clientes que tienen un valor de TotalHistorico_CompradoCliente similar, lo que indica que algunos clientes gastan más que otros para un número similar de compras. Esto puede estar influenciado por factores como el tipo de producto comprado o la elección de productos premium frente a económicos.
Se observa una concentración de clientes que han gastado históricamente alrededor de 45 unidades y que también han comprado en cantidades elevadas.
Estos clientes pueden ser candidatos ideales para programas de fidelización, recompensas o servicios premium, ya que han demostrado un alto compromiso con la tienda.
En la parte inferior izquierda del gráfico, se encuentra un grupo considerable de clientes con un TotalHistorico_CompradoCliente relativamente bajo (15-25) y un gasto histórico entre 20 y 35. Estos clientes podrían estar realizando compras más esporádicas o comprando productos más económicos.
Este grupo podría ser un objetivo para aumentar su gasto y frecuencia de compra mediante campañas de marketing dirigidas, como promociones o descuentos específicos.
Segmentación basada en comportamiento: Usar esta correlación para segmentar a los clientes en categorías de alto y bajo valor podría ayudar a personalizar estrategias de retención y adquisición.''')

def mensaje_grafico_dispersion_Cant(cluster, tipo):
   if(cluster==0):
        if(tipo=='Standard'):
            print('''El gráfico muestra la relación entre las cantidades totales solicitadas utilizando el método de envío estándar y el gasto histórico total de los clientes.
Se observa que esta relación se mantiene relativamente uniforme, ya que el gasto total no muestra un incremento o disminución clara a medida que aumenta la cantidad solicitada a través de este método.
Esto indica que el método de envío estándar no parece ser un factor determinante que influya significativamente en el comportamiento de gasto de los clientes.
Aunque el volumen de pedidos puede variar, el gasto permanece estable, lo que sugiere que este método no logra incentivar un mayor gasto por parte de los clientes.
Una forma de mejorar esto podría ser introduciendo incentivos asociados al método estándar, como descuentos por volumen o beneficios adicionales.''')
        elif(tipo=='Urgent-Delivery'):
           print('''A diferencia del gráfico anterior, las cantidades totales solicitadas utilizando el método de envío urgente parecen mostrar una relación positiva con el gasto histórico total de los clientes.
Se observa que el gasto total tiende a incrementarse ligeramente conforme aumenta la cantidad solicitada a través de este método.
Esto sugiere que el método de envío urgente puede influir, aunque de manera leve, en el comportamiento de gasto de los clientes.
Una posible explicación es que los clientes que optan por este método pueden tener necesidades inmediatas que requieren atención rápida.
Y teniendo en cuenta que el envío urgente suele tener un costo mayor en comparación con el estándar, los clientes podrían estar más predispuestos a realizar compras adicionales o de mayor valor para justificar el costo elevado del envío.
Se podría entonces, ofrecer paquetes promocionales o artículos complementarios, incentivando la compra de productos relacionados con los que ya están en el carrito, aprovechando el contexto de la necesidad urgente.
Sugerir productos que históricamente han sido comprados junto con aquellos seleccionados para envío urgente, optimizando la experiencia de compra.''')


def mensaje_grafico_forma_pago(cluster):
   if(cluster==0):
      print('''En general, el crédito es el método de pago más utilizado en los diferentes géneros y categorías de ingresos.
Este predominio es más evidente en el caso del género masculino, donde las diferencias entre el gasto con crédito y otros métodos (efectivo y débito) son mucho mayores. Esto sugiere que los hombres tienden a preferir el crédito de manera consistente, sin importar su nivel de ingresos.
Dado su fuerte uso de crédito, se podría incentivar este grupo mediante convenios con emisores de tarjetas de crédito que ofrezcan beneficios exclusivos, como puntos de recompensa o descuentos en compras específicas. Esto podría fidelizar a estos clientes y aumentar el gasto.
Se observa que las mujeres con ingresos altos, bajos e indeterminados utilizan más frecuentemente el débito que los hombres, siendo menores la diferencias entre los grupos.
Para aquellas con ingresos bajos, sería beneficioso ofrecer descuentos por pagos al contado o promociones especiales para quienes usen débito. Esto podría ajustarse a su preferencia por pagos más directos.
El grupo de genero indeterminado presenta una distribución más balanceada entre los tres métodos de pago, sin una diferencia tan marcada como en los otros géneros.
Dado su comportamiento variado, se podrían implementar promociones que beneficien todos los métodos de pago, asegurando que ningún cliente se sienta excluido.
Los clientes con ingresos medios parecen ser los que gastan más, independientemente del género. Esto sugiere que podrían ser un segmento clave para enfocar estrategias de marketing, adaptadas a sus métodos de pago preferidos.
''')

def mensaje_graficoEstacion(cluster):
   if(cluster==0):
      print('''En general, Otoño y Primavera tienden a ser las estaciones predominantes en términos de gasto, aunque las diferencias con Invierno y Verano no son extremadamente marcadas.
Lanzar campañas específicas que promuevan productos relevantes para las estaciones predominantes, como ropa de abrigo en Otoño y accesorios para el calor en Primavera.
Ofrecer promociones de "transición de temporada" en productos que los clientes podrían necesitar antes del cambio de estación.
Introducir programas de pre-compra que permitan a los clientes adquirir productos para la próxima temporada a precios especiales, asegurando un flujo constante de ingresos.
Incentivar las compras a través de descuentos en productos de temporadas anteriores, atrayendo especialmente a los segmentos con ingresos bajos e indeterminados.''')


def mensaje_graficoMomentoDia(cluster):
  if (cluster==0):
    print('''Ofrecer a las mujeres dentro de la categoria Adulto Joven de ingresos medios y altos, productos que sean de su interes,  hacerlo en la madrugada y la mañana, cuando mas se compra. Para ello es necesario estudiar los productos que se compran.
Estudiar si las personas que compran al medioDia y en la tarde son de otro grupo de edad y que productos se compra.''')


def mensajeGenero_edad_Hora(pais, genero, edad, cluster):
  if(cluster==0):
    print(f'''La mayoría de las personas que viven en {pais} y son del género {genero}, que pertenecen al grupo {edad} compran en la mañana y la madrugada, seguido por la tarde.''')





def mensaje(num):
    if(num==1):
        return '''Análisis de comportamiento de compra en mujeres jóvenes y adultas en USA:
    En los Estados Unidos, hay una alta representación de mujeres jóvenes y adultas con ingresos elevados que compran principalmente
    en las primeras horas del día, especialmente durante la madrugada y la mañana.
    Estas consumidoras se enfocan en diversas categorías de productos, con particular preferencia por alimentos, ropa y libros.
    Los Alimentos son la categoría más comprada por este grupo.
    Ropa y libros, le siguen en popularidad. Existe una oportunidad para ofrecer estos productos con una plataforma que permita tanto
    la compra de artículos nuevos como la reventa de productos usados, incentivando así un ciclo de consumo sostenible.
    También podría considerarse la integración de libros electrónicos (e-books) en la plataforma.
    Decoración del hogar, muebles y electrodomésticos: Aunque estos productos tienden a ser más costosos, presentan alta rotación.
    Esto sugiere que estas compradoras buscan productos en tendencia, de calidad y que reflejen un interés en la moda y el diseño.
    Sería beneficioso ofrecer artículos de vanguardia que satisfagan esta demanda.
    Productos electrónicos (audio, smartphones y televisores): Estos productos, aunque presentan pocas cantidades vendidas, tienen un impacto
    significativo en los ingresos de la empresa, ya que pequeños aumentos en las unidades vendidas pueden significar cambios mayores en la rentabilidad de la empresa.
    En particular, los smartphones son altamente rentables, ya que ocupan poco espacio de almacenamiento y son fáciles de transportar.
    Una estrategia atractiva podría ser la oferta de un plan de recambio anual, en el cual las clientas puedan obtener el último modelo de teléfono
    al entregar su dispositivo usado, que a su vez podría repararse y revenderse a clientes de ingresos más bajos.
    Además, se podrían ofrecer descuentos en audífonos al comprar un smartphone o parlantes con la compra de un televisor.
    La mayoría de estas consumidoras opta por pagar con crédito.
    Las ciudades con mayor representatividad en este grupo son Boston y Chicago. Aunque el nivel de satisfacción es bueno en ambas,
    se observa una porción de clientes insatisfechas. Esto abre una oportunidad para investigar las causas de esta insatisfacción, diferenciando
    las características de estos grupos para mejorar la experiencia de compra. Si no se cuenta con más información al respecto, podría ser útil
    enviar un cuestionario de satisfacción acompañado de un incentivo, como un descuento en alimentos, libros o ropa, para animar la participación.
    Como estas compradoras tienden a realizar sus compras en la madrugada y la mañana, sería conveniente implementar un carrito de compras programado.
    Este podría optimizar el tiempo de búsqueda, sugiriendo automáticamente productos que suelen comprar y dejando espacio para descubrir nuevos
    artículos o recomendaciones personalizadas en función de sus preferencias. Esto permitiría una experiencia de compra eficiente y atractiva.
    '''
    elif(num==2):
        return '''Análisis de satisfacción y optimización de envíos en diferentes categorías de productos:.
    Se observa que las clientas de ingresos altos están muy satisfechas con el servicio de entrega para productos de electrodomésticos (Appliances).
    Sin embargo, en las categorías de Books y Food, la diferencia en satisfacción es menor, lo que podría indicar problemas en el servicio de envío
    específico para estos productos. En la categoría de Clothing, el índice de satisfacción es significativamente mejor, lo que sugiere que el proceso
    de entrega para ropa se maneja con mayor eficacia que en las otras categorías.
    Para optimizar la satisfacción de las clientas y mejorar la eficiencia en los envíos, podría ser beneficioso implementar una plataforma de
    alquiler de libros online. Esto permitiría a las clientas alquilar libros junto con sus compras de ropa, combinando envíos y disminuyendo
    la carga logística en momentos de alta demanda.
    En caso de que la empresa experimente saturación de entregas en ciertos momentos del día, podría ser útil incentivar la compra de artículos
    menos urgentes, como libros, junto con productos de alta demanda. Esto permitiría agrupar envíos y liberar recursos para atender otras categorías
    con mayor rapidez.
    Para ofrecer mayor conveniencia a las clientas, podría implementarse un sistema de casilleros en lugares estratégicos de la ciudad.
    De esta forma, las clientas podrían retirar sus pedidos en el horario que más les convenga, reduciendo la presión sobre el sistema de entregas
    y mejorando la experiencia del cliente al permitirle flexibilidad en la recogida de sus productos.
    '''
    elif(num==3):
        return '''El gráfico muestra que los clientes insatisfechos representan casi el 80% de la cantidad de clientes satisfechos, lo cual indica una
    deficiencia significativa en el servicio de envíos. Este dato sugiere que es crucial mejorar la calidad de entrega, especialmente en las
    ciudades de Chicago y Boston, donde se concentra la mayor cantidad de clientes.
    Foco en Chicago y Boston: Dado que estas ciudades presentan el mayor volumen de clientes, es prioritario optimizar el servicio de entrega
    en estas áreas para reducir la insatisfacción. Identificar las causas de los problemas actuales en la logística de envío (como demoras,
    entregas fallidas o falta de opciones flexibles) sería fundamental para mejorar la experiencia de los clientes y fortalecer la retención.
    Expansión en San Francisco: La ciudad de San Francisco es un mercado con gran potencial de crecimiento, especialmente por su población
    predominantemente joven, que valora la flexibilidad y las opciones de conveniencia. Implementar casilleros de recogida en puntos estratégicos
    de la ciudad podría mejorar la experiencia del cliente, permitiéndole retirar sus pedidos en el momento que más le convenga y facilitar el
    proceso de devolución. Estos casilleros podrían situarse en ubicaciones clave, como estaciones de transporte público, gimnasios y áreas de
    trabajo, para adaptarse al estilo de vida activo y dinámico de estos clientes.
    Además de brindar conveniencia a los clientes, los casilleros reducirían la presión sobre el sistema de entregas al disminuir el número de
    envíos a domicilio y facilitar la logística de devoluciones. Los clientes podrían gestionar sus devoluciones fácilmente mientras realizan
    otras actividades cotidianas, lo que aumentaría la eficiencia operativa y mejoraría la satisfacción general con el servicio.
    '''

    elif(num==4):
        return
    elif(num==5):
        return
    elif(num==6):
        return

#----------------------------------


def resultMensaje(genero, ingreso, valor, pais):

    if(genero=='Female'):
        if(ingreso=='High'):
            if(valor=='Joven'):
                print(mensaje(1))
            elif(valor=='Adulto'):
                print(mensaje(2))
        elif(ingreso=='Low'):
            if(valor=='Joven'):
                print(mensaje(3))
            elif(valor=='Adulto'):
              print(mensaje(3))
        elif(ingreso=='Indeterminate'):
            if(valor=='Joven'):
                print(mensaje(3))
            elif(valor=='Adulto'):
              print(mensaje(3))
    else:
        return ''




def mensajePaisGenero(cluster, pais, genero):
  if(cluster==0):
    print(f'''La mayoría de las personas que viven en {pais} y son del género {genero}, pertenecen al grupo Joven y Adulto_Joven''')

