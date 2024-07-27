- [x] Limpieza de datos
- [] Hacer el EDA
- [] Probar modelo Kmeans
- [] Evaluar metodo del codo
- [] Evaluar silueta
- [] Probar modelo K-Prototypes
- [] Evaluar metodo del codo
- [] Evaluar silueta
- [] Analizar cual modelo es mejor
- [] Analizar los clusters
 
Ideas objetivos
Categoria deportistas, evento deportivo, ofrecer productos antes
Fijar patrones de compras segun clima
 
# Entendimiento del Negocio
 
Se trata de una empresa que se dedica al rubro de venta online. Compra y disponibiliza los productos en su plataforma para que los clientes compren con mejor comodidad, facilidad y rapidez.
 
# Problema
Con el crecimiento exponencial de las plataformas de ventas online, las empresas se enfrentan cada vez más a la necesidad de comprender los patrones de consumo, identificar oportunidades de ventas y optimizar los procesos productivos.
 
En este análisis, me gustaría centrar la atención en la clasificación de los distintos tipos de clientes. Entender quiénes son los clientes, qué compran y por qué, permite a las empresas diseñar estrategias personalizadas que pueden aumentar la satisfacción del cliente, fomentar la lealtad y, en última instancia, impulsar las ventas.
 
# 1.1 Alcance
 
# 1.1.1 Objetivo
 
Cuando una empresa competitiva busca optimizar sus beneficios, tiene varias estrategias a su disposición. Los beneficios se definen como la diferencia entre ingresos y costos. Los ingresos se calculan como el precio multiplicado por la cantidad vendida (I=p×q).
Para incrementar los ingresos, la empresa puede optar por aumentar el precio, aumentar la cantidad vendida, o una combinación de ambos.
 
La decisión sobre cuál estrategia seguir debe considerar la elasticidad-precio de la demanda, que mide cómo varía la cantidad demandada ante cambios en el precio.
Si la elasticidad-precio de la demanda es alta (demanda elástica), un aumento en el precio llevará a una reducción proporcionalmente mayor en la cantidad demandada, lo que puede resultar en una disminución de los ingresos totales. En cambio, si la elasticidad-precio de la demanda es baja (demanda inelástica), el aumento del precio puede llevar a un incremento en los ingresos, ya que la reducción en la cantidad demandada será menor que el aumento en el precio.
 
Para productos con demanda inelástica, la empresa puede justificar un aumento de precio para maximizar los ingresos, siempre y cuando el incremento en el precio no resulte en una caída significativa en la cantidad demandada. En cambio, para productos con demanda elástica, es crucial enfocarse en estrategias que minimicen los costos y maximicen el volumen de ventas.
 
En el caso de productos con demanda elástica, una estrategia viable podría ser la reducción de costos variables. La disminución de costos variables implica ajustar la cantidad ofertada. Si la empresa opera bajo un modelo de tercerización, donde no produce directamente los bienes, puede implementar ajustes rápidos en la oferta de productos sin necesariamente aumentar costos. Por ejemplo, podría optimizar el proceso de logística y distribución para reducir el costo variable por unidad. Esto incluye agrupar envíos para atender múltiples pedidos con un solo traslado, lo que disminuirá los costos de transporte y distribución.
 
Adicionalmente, la reducción de costos fijos puede ser considerada, aunque esto generalmente requiere una planificación a largo plazo y puede implicar cambios estructurales en la empresa.
 
Por lo tanto, la empresa debe estudiar las siguientes estrategias:
 
Incrementar precios en productos con demanda inelástica: Analizar cómo las variaciones de precio afectan la cantidad demandada y ajustar los precios para maximizar los ingresos.
 
Aumentar la cantidad vendida de productos: Evaluar si es posible incrementar el volumen de ventas sin que esto implique un aumento proporcional en los costos.
 
Optimizar el proceso de distribución: Implementar estrategias logísticas para reducir los costos variables asociados con el transporte, como consolidar envíos y mejorar la eficiencia en la cadena de suministro.


# 1.1.2 Hipótesis

Ligadas a las características de la orden

H1. El importe gastado en la orden puede ayudar a identificar patrones de consumo entre los usuarios.
H2. La cantidad comprada de productos es un factor que permite definir perfiles de compradores.
H3. Los tipos de productos y las características inherentes a los productos comprados ayudan a explicar patrones de consumo.
H4. El tipo de envío solicitado para la entrega del pedido.
H5. Las promociones o descuentos aplicados en la compra permiten identificar la sensibilidad al precio y la respuesta a estrategias de marketing.
H6. Las categorías de productos más compradas pueden indicar intereses y necesidades predominantes entre diferentes grupos de compradores.
H7. El valor promedio del carrito de compras proporciona insights sobre el poder adquisitivo y las tendencias de gasto de los clientes.

Ligadas a las características del usuario

H8. El método de pago utilizado en la transacción es un factor determinante para analizar tipos de consumidores.
H9. La frecuencia de compras puede revelar la lealtad del cliente y su comportamiento de compra recurrente.
H10. El historial de compras del consumidor
H11. El poder adquisitivo del cliente permite identificar patrones de consumo.
H12. Las características demográficas del comprador, como edad, género y ubicación, permiten segmentar a los clientes en grupos específicos.

Ligadas al contexto

H13. La estacionalidad de las compras proporcionan información sobre preferencias estacionales y ciclos de compra.
H14. Las horas y días de la semana en que se realizan las compras pueden ofrecer información sobre los hábitos y comportamientos de compra.
H15. El clima puede ser un factor determinante por el cual se dan determinadas compras.

# 1.1.3 Limitantes
