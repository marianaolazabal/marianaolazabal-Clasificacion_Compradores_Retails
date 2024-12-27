def mensaje_graficoGasto_cliente(cluster):
  if(cluster==0):
    print('''
Los porcentajes indican qué fracción del gasto total en cada grupo es atribuible a los diferentes géneros.
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

    print('''
Se observa una alta representatividad de la categoría "Joven", en todos los países. Siendo en Alemania,
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
    print('''
Como se puede apreciar en el gráfico, la distribución de gasto en los jóvenes es muy parecida, tanto para mujeres como hombres.
En el caso de Adulto-Joven, las mujeres gastan un poco más que los hombres.
En los adultos, adultos mayores y veteranos, los hombres gastan más.
El grupo de género indeterminado se encuentra con una distribución menos dispersa, no presenta casi datos atípicos y en general gastan lo mismo o en el caso de los adultos y veteranos, más que los otros
géneros. Se recomienda replantear la descripción de género para ser más inclusivo con el grupo y aplicar publicidades destinadas a aumentar la participación de personas de este grupo.''')



def mensaje_grafico_gastos_genero_ingreso(cluster):
  if(cluster==0):
    print('''
En el caso de la distribucion del gasto por genero y grupo de ingresos, se observa que las personas que pertenecen al
genero Femenino y el grupo de ingresos altos, tienden a gastar mas que los hombres y personas del genero indeterminado.
Teniendo en cuenta el grafico anterior, podria ser beneficioso realizar campañas de marketing apuntadas a ofrecer
productos premium, a personas dentro de estas categorias.
    ''')


def mensaje_grafico_productos_mas_comprados(cluster):
  if(cluster==0):
    print('''
Las categorías de Food y Clothing son las más compradas en todos los grupos de ingresos. Lo que hace que sea crucial prestar atención al stock de estos productos para garantizar su disponibilidad.
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
    print('''
El gráfico muestra una clara correlación positiva entre la cantidad total comprada y el gasto histórico del cliente. Ademas muestra como el tamaño de los circulos aumentan conforme aumenta la frecuencia de compra.
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
            print('''
El gráfico muestra la relación entre las cantidades totales solicitadas utilizando el método de envío estándar y el gasto histórico total de los clientes.
Se observa que esta relación se mantiene relativamente uniforme, ya que el gasto total no muestra un incremento o disminución clara a medida que aumenta la cantidad solicitada a través de este método.
Esto indica que el método de envío estándar no parece ser un factor determinante que influya significativamente en el comportamiento de gasto de los clientes.
Aunque el volumen de pedidos puede variar, el gasto permanece estable, lo que sugiere que este método no logra incentivar un mayor gasto por parte de los clientes.
Una forma de mejorar esto podría ser introduciendo incentivos asociados al método estándar, como descuentos por volumen o beneficios adicionales.''')
        elif(tipo=='Urgent-Delivery'):
           print('''
A diferencia del gráfico anterior, las cantidades totales solicitadas utilizando el método de envío urgente parecen mostrar una relación positiva con el gasto histórico total de los clientes.
Se observa que el gasto total tiende a incrementarse ligeramente conforme aumenta la cantidad solicitada a través de este método.
Esto sugiere que el método de envío urgente puede influir, aunque de manera leve, en el comportamiento de gasto de los clientes.
Una posible explicación es que los clientes que optan por este método pueden tener necesidades inmediatas que requieren atención rápida.
Y teniendo en cuenta que el envío urgente suele tener un costo mayor en comparación con el estándar, los clientes podrían estar más predispuestos a realizar compras adicionales o de mayor valor para justificar el costo elevado del envío.
Se podría entonces, ofrecer paquetes promocionales o artículos complementarios, incentivando la compra de productos relacionados con los que ya están en el carrito, aprovechando el contexto de la necesidad urgente.
Sugerir productos que históricamente han sido comprados junto con aquellos seleccionados para envío urgente, optimizando la experiencia de compra.''')


def mensaje_grafico_forma_pago(cluster):
   if(cluster==0):
      print('''
En general, el crédito es el método de pago más utilizado en los diferentes géneros y categorías de ingresos.
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
      print('''
En general, Otoño y Primavera tienden a ser las estaciones predominantes en términos de gasto, aunque las diferencias con Invierno y Verano no son extremadamente marcadas.
Lanzar campañas específicas que promuevan productos relevantes para las estaciones predominantes, como ropa de abrigo en Otoño y accesorios para el calor en Primavera.
Ofrecer promociones de "transición de temporada" en productos que los clientes podrían necesitar antes del cambio de estación.
Introducir programas de pre-compra que permitan a los clientes adquirir productos para la próxima temporada a precios especiales, asegurando un flujo constante de ingresos.
Incentivar las compras a través de descuentos en productos de temporadas anteriores, atrayendo especialmente a los segmentos con ingresos bajos e indeterminados.''')


def mensaje_graficoMomentoDia(cluster):
  if (cluster==0):
    print('''
Ofrecer a las mujeres dentro de la categoria Adulto Joven de ingresos medios y altos, productos que sean de su interes,  hacerlo en la madrugada y la mañana, cuando mas se compra. Para ello es necesario estudiar los productos que se compran.
Estudiar si las personas que compran al medioDia y en la tarde son de otro grupo de edad y que productos se compra.''')


def mensajeGenero_edad_Hora(pais, genero, edad, cluster):
  if(cluster==0):
    if(pais=='United States'):
        if(genero=='Female'):
            if(edad=='Adulto_Joven'):
               print(f'''
La mayoría de las personas que viven en United States, del genero Femenino, dentro de la categoría Adulto_Joven
compran en la mañana y la madrugada, seguido por la tarde.''')
            elif(edad=='Joven'):
               print(f'''
La mayoría de las personas que viven en United States, del genero Femenino, dentro de la categoría Joven
compran en la madrugada y la mañana, seguido por la tarde. La diferencia con el grupo Adulto_Joven es que compran
en mayor porcentaje en la madrugada. Esto podría estar indicando que son personas que trabajan tarde o estudian y realizan
compras espontáneas. Se podría a futuro, permitir guardar direcciones dentro de la aplicación, para distinguir entre casa o trabajo y 
con esto, identificar si hay grupos de oficio que expliquen comportamientos de compras nocturnos.''')
    elif(pais=='United Kingdom'):
        if(genero=='Female'):
            if(edad=='Joven'):
                print('''La mayoría de las personas que viven en United Kingdom, del genero Femenino, dentro de la categoría Joven
compran en la madrugada, la tarde y la mañana.''')


def mensaje_estuadio_ingresos(ingreso, edad, pais, genero, cluster):
 
    if(cluster==0):
        print('''
Análisis de Comportamiento de Compra en Mujeres Jóvenes y Adultas en Estados Unidos y Reino Unido
Patrones Generales y Preferencias de Productos

Las categorías más populares entre las mujeres jóvenes y adultas, tanto en Estados Unidos como en el Reino Unido, son Comida, Libros y Ropa. Esto sugiere que la plataforma ofrece una amplia variedad de productos atractivos y relevantes para diferentes niveles de ingresos. Además, se observa que el precio no parece ser un factor determinante en las decisiones de compra, lo que abre oportunidades para mejorar otros aspectos como la rapidez de los envíos, la experiencia del usuario y la atención al cliente.
Análisis Geográfico y Satisfacción por Ciudad

Estados Unidos:

    Chicago y Boston:
    Estas ciudades presentan una alta representatividad de clientes. Aunque los niveles de satisfacción son buenos en general, existe un equilibrio entre satisfacción e insatisfacción. Es necesario investigar las causas detrás de esta inconformidad para mejorar la experiencia del cliente en estas regiones.
    Charlotte:
    Se detecta insatisfacción total en esta ciudad, lo que evidencia problemas significativos relacionados con el servicio, como logística o disponibilidad de productos.
    Baltimore, Dallas y otras ciudades menores:
    Los niveles de satisfacción son altos, lo que contrasta con los resultados observados en Chicago y Charlotte. Estas diferencias sugieren que factores específicos, como las condiciones locales o la operación logística, afectan la percepción del servicio.

Reino Unido:

    Birmingham, Leeds y Liverpool:
    Aunque se mantienen los productos más populares, estas ciudades muestran una mayor proporción de insatisfacción entre clientas de ingresos altos. Este fenómeno representa una oportunidad para adaptar estrategias que mejoren la experiencia en estas regiones.
    Belfast:
    Este grupo, perteneciente al segmento de ingresos indeterminados, muestra bajos niveles de satisfacción. Identificar las razones detrás de los buenos resultados en ciudades como Birmingham y Brighton, donde se reporta un 100% de satisfacción, podría ofrecer aprendizajes clave para abordar estas áreas problemáticas.
    Edimburgo:
    Las clientas con ingresos bajos en esta ciudad expresan altos niveles de satisfacción, lo que podría indicar que estas zonas tienen una mayor representatividad de este segmento o una falta de alternativas competitivas al servicio ofrecido.

Recomendaciones Estratégicas

    Investigación y Mejora del Servicio en Zonas Problemáticas:
    Es crucial realizar estudios en ciudades como Charlotte y Belfast para identificar factores que contribuyen a la insatisfacción, como problemas de logística, calidad del servicio o diferencias culturales.

    Fortalecimiento de la Logística:
        Implementar un sistema de casilleros estratégicamente ubicados en ciudades como Chicago y Boston, permitiendo a las clientas recoger sus pedidos a conveniencia y reduciendo la presión sobre el sistema de entregas.
        Optimizar los envíos combinando productos de baja urgencia (como libros) con productos de alta demanda, lo que podría aliviar saturaciones en momentos pico.

    Innovaciones en la Plataforma:
        Incorporar una funcionalidad de carrito de compras programado para clientas que compran en horas tempranas, mejorando la experiencia al sugerir productos basados en compras previas y preferencias.
        Ofrecer un modelo de reventa y alquiler de productos, como libros y smartphones, incentivando un consumo más sostenible.

    Estrategias de Incentivos:
        Enviar cuestionarios de satisfacción acompañados de descuentos en las categorías más populares (Comida, Libros y Ropa) para motivar la participación y recopilar insights valiosos.
        Diseñar campañas que destaquen la posibilidad de recambio anual de dispositivos electrónicos, acompañadas de promociones cruzadas, como descuentos en audífonos o parlantes.

    Adaptación a Segmentos y Regiones:
        Aprovechar el alto nivel de satisfacción en ciudades como Birmingham y Brighton para replicar prácticas exitosas en áreas de bajo desempeño.
        En regiones con alta representatividad de clientas de ingresos bajos, considerar el lanzamiento de campañas con descuentos y promociones para estimular el consumo.''')

    elif(cluster==1):
       print('''''')









def mensajePaisGenero(cluster, pais, genero):
  if(cluster==0):
    print(f'''La mayoría de las personas que viven en {pais} y son del género {genero}, pertenecen al grupo Joven y Adulto_Joven''')

