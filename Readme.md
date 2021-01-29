CryptoCompare
Descripción general
La aplicación web, que compara los contratos de minería en la nube ofrecidos por diversas empresas mineras. La aplicación también ofrece la lista de monedas digitales con sus precios actuales, breve descripción, tasas de hash, oferta actual, etc. También hay lista de empresas que brindan información de shotr sobre las empresas mineras y los contratos que ofrecen. Todos los contratos listados dentro de una empresa se muestran en términos de monedas. El usuario también puede ver una lista completa de contratos y detalles de cada contrato.

Un usuario puede elegir dos contratos y comparar sus rendimientos diarios, semanales y mensuales, así como el beneficio y la rentabilidad totales.

La comparación se realiza utilizando no solo los precios actuales de las monedas digitales ofrecidas, sino también la predicción respaldada por IA. Para calcular las tarifas de precios futuros en la aplicación, utilizamos la red neuronal recurrente neuronal de memoria a largo plazo

Tecnologias
FRONTEND se hace usando principalmente Vue.js con algo de JQuery. Utiliza la biblioteca cliente https de Axios para consumir API REST.

BACKEND. Para la tecnología de backend, se eligió Python Django. Consulta una base de datos, procesa datos y los vuelve a publicar como objetos JSON.

BASE DE DATOS. Como base de datos, elegimos MongoDB como programa de base de datos orientado a documentos multiplataforma NoSQL.

Recursos externos
La plantilla HTML del sitio web está diseñada por ColorLib . El sitio web, además de utilizar la API REST del backend del sitio web, también consume API de terceros:

coingecko.com para obtener información sobre los indicadores del mercado de monedas
rapidapi.com para obtener información técnica sobre monedas
