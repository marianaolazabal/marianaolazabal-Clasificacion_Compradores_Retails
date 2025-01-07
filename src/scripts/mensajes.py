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


def mensaje_estuadio_ingresos(cluster):
 
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
        En regiones con alta representatividad de clientas de ingresos bajos, considerar el lanzamiento de campañas con descuentos y promociones para estimular el consumo.
              
    Del análisis del top 10 de productos más comprados, se identifica que las categorías Food y Books son las más populares entre el grupo femenino Adulto-Joven con ingresos altos en Estados Unidos. 
Este grupo se concentra principalmente en la ciudad de Chicago y, en general, está satisfecho con el servicio. 
Sin embargo, se observa un porcentaje de personas dentro de este segmento que se encuentra insatisfecho. 
Se recomienda investigar a fondo las causas de esta inconformidad.

Del análisis del top 10 de productos más comprados, se identifica que las categorías Food y Ropa son las más populares entre el grupo femenino Adulto-Joven con ingresos bajos en Estados Unidos. 
Este grupo se encuentra mayoritariamente en la ciudad de Chicago, donde la mayoría reporta estar satisfecha con el servicio. 
Sin embargo, se destaca un porcentaje significativo de clientas que manifiestan insatisfacción, lo que sugiere la necesidad de investigar en profundidad las posibles causas detrás de este descontento.
Además, se identificó a clientas de este segmento ubicadas en otras ciudades como Baltimore, Charlotte y Dallas. 
Todas ellas reportaron estar satisfechas con el servicio, lo que contrasta con los resultados observados en Chicago.
A medida que se mejore la representatividad de estas ciudades en el análisis, será posible evaluar las diferencias entre estas ubicaciones y explorar factores específicos que puedan estar contribuyendo a la insatisfacción en Chicago.

                      Del análisis se desprende que las categorías de productos más comprados son Food y Furniture. 
Sin embargo, la percepción del servicio varía significativamente según la ubicación geográfica.
En el caso de Chicago, las opiniones del grupo están divididas entre satisfacción e insatisfacción, lo que sugiere que existen factores específicos que generan experiencias inconsistentes. 
Por otro lado, en Charlotte, se destaca una insatisfacción total dentro de este segmento, lo cual evidencia un problema más profundo que requiere atención inmediata.
Estos hallazgos apuntan a la necesidad de realizar un análisis detallado de las condiciones en ambas ciudades, considerando aspectos como el nivel de servicio, la disponibilidad de productos, el tiempo de entrega, y las expectativas de los clientes. 
Una investigación más exhaustiva podría ayudar a identificar las causas subyacentes de la insatisfacción y proporcionar soluciones adaptadas a las necesidades específicas de cada mercado.

Análisis de comportamiento de compra en mujeres jóvenes y adultas en USA:
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

Se observa una alta representatividad de clientes en Chicago, seguida de Boston, donde los niveles de satisfacción e insatisfacción presentan una distribución muy equilibrada.
Al igual que en otros grupos analizados, los productos más populares son Comida, Libros y Ropa. 
Este comportamiento podría indicar que la plataforma ofrece una amplia y atractiva variedad de productos dentro de estas categorías, lo que capta el interés de un público diverso. 
Otra interpretación posible es que estos productos son percibidos como relevantes y accesibles para diferentes niveles de ingreso, lo que implica que el precio no es un factor determinante en las decisiones de compra.
Este hallazgo abre oportunidades para un análisis más profundo sobre la estrategia de precios y la diversidad de productos ofrecidos. 
Si el precio no influye significativamente en las decisiones de compra, la plataforma podría considerar enfocarse en otros factores diferenciadores, como la experiencia del usuario, la rapidez en los envíos o la calidad del servicio al cliente, para fortalecer su posicionamiento.

Análisis de satisfacción y optimización de envíos en diferentes categorías de productos:.
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

Como se observa de los graficos, se mantienen los productos mas populares para las mujeres que vivien en el Reino Unido y tienen ingresos altos, 
mientras que muchas expresan satisfacción con su experiencia de compra, en ciudades como Birmingham, Leeds y Liverpool se observa una mayor proporción de insatisfacción, lo que representa una oportunidad para mejorar la experiencia del cliente en esas áreas. 
Estas tendencias nos permiten adaptar estrategias para ofrecer productos y servicios que se alineen aún más con las necesidades y horarios de este segmento.
En el caso de las clientas que pertencen al segmento de bajos ingresos se muestra una representatividad mayor en Birmingham y la satisfaccion es tambien mayor para esta ciudad, al igual que Edinburgh que no figura en ingresos altos, esto puede estar indicando que son ciudades con mayor representatividad de ingresos bajos o no hay alternativas al servicio, esto abre una oportunidad para mejorar en la zona, ofreciendo descuentos e incentivos que estimulen la compra de productos.
Se observa gran representatividad en la ciudad de Belfast del grupo de ingresos indeterminados, sin embargo el nivel de Satisfaccion es bajo, identificar por que ciudades como Birmingham y Brighton tienen un nivel de satisfaccion del 100 % podria ayudar a mejorar.
                        
    Ropa, Electrodomesticos y comida son los productos mas comprados entre las personas de la categoria Adulto y veterano del genero femenino.
Se encuentran en 5 ciudades, Memphis y Portland son ciudades con un nivel de insatisfaccion importante, esto puede ser por falta de productos, problemas en los envios, etc.
Las personas adultas parecen estar en su mayoria mas insatisfechas, esta puede ser la razon por la que hay baja representatividad del grupo. Tanto Estados Unidos como 
el Reino Unido tienen este problema, siendo que en general compran articulos de mauor tama;o, como electrodomesticos y muebles, que a si mismo son mas caros, es posible que 
el servicio esta funcionando correctamente para los productos peque;os pero no para los grandes. Esto puede deberse a un problema en el envio, en el stock, en el precio u otros. 
Estudiar con mayor detenimiento puede ayudar a mejorar el servicio y eventualmente las ventas para este grupo.
              
              
Del genero masculino:
              
Tambien hay mayor representatividad de jovenes y adultos jovenes, se encuentran localizados en United States y United Kingdom, seguido por Germany.
Boston y Chicago siguen siendo las ciudades con mayor representatividad pero ahora aparece San Francisico, esto es importante ya que es un lugar donde predomina poblacion joven, nativa a la tecnologia, por lo que hay potencial para expandir.
Encontrar las razones por las insatisfacciones podrian ser clave para mejorar.
              
Chicago es la cuidad con mayor representatividad en ingresos bajos, tener en cuenta que los ingresos en cada ciudad pueden variar, lo importante es el ingreso real, ingreso vs cuanto puede comprar el ingresi en esa ciudad. Considerar entonces explorar productos diferenciados para que sean accesibles a un publico con menor ingreso.

Para el grupo de genero masculino con ingresos altos y categoria de edad adulto, se observa que hay ciudades con alto nivel de satisfaccion y otras no. Al igual que en el caso del genero femenino, se recomienda estudiar las diferencias entre las ciudades para atender el problema. 

Para el caso de adultos con ingresos bajos, aparecen ciudades que no figuran en otros segmentos, esto puede estar informando que hay productos de bajo costo que los de ingresos altos los perciben de mala calidad y no los compran, en contraposicion a los de ingresos bajos que si los compran y estan muy satisfechos. 
Explorar la posibilidad de diferenciar a los clientes para bajar la percepcion del grupo con ingresos altos, ofrecer perfil premium para ver productos diferenciados, de alta calidad y nuevos.

El grupo de ingresos intermedios esta dividido en Boston y Nashville, uno esta totalmente satisfecho y el otro no, sin emabrgo esto puede deberse a la baja representatividad del grupo.

En United Kingdom aparece para el grupo joven de ingresos altos, en 4to lugar los smart phone, este podria ser un buen lugar para planificar una prueba de recambio de celulares. Se observa satisfaccion general en las ciudades, sin embargo, Portsmouth, Brighton y Birmingjam son las que tinen un nivel de satisfacicon mas elevado. Se podria probar en una de estas ciudades y otra que tenga un nivel de saisfaccion menor pero que el consumo de smart phones sea elevado para estudiar la incidencia de la promocion.

''')


    elif(cluster==1):
       print('''''')









def mensajePaisGenero(cluster, pais, genero):
  if(cluster==0):
    print(f'''La mayoría de las personas que viven en {pais} y son del género {genero}, pertenecen al grupo Joven y Adulto_Joven''')
