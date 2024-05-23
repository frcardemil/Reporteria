document.addEventListener('DOMContentLoaded',function() {
  
  // Datos del gráfico
  const datos = [20, 30, 40, 50, 60, 70,100];
  const labels = ['A', 'B', 'C', 'D', 'E','F','g'];
  const nameLabel = 'Los cara floja'

  addGrafico('myChart',datos,labels,nameLabel);
})
function addGrafico(nameID,listaData,listaNameData,nombreLabel){
   // Obtener el contexto del canvas
   const ctx = document.getElementById(nameID).getContext('2d');

   // Crear el gráfico con Chart.js
   const miGrafico = new Chart(ctx, {
       type: 'line', // Cambia a 'line' para un gráfico de líneas, etc.
       data: {
           labels: listaNameData,
           datasets: [{
               label: nombreLabel,
               data: listaData,
               backgroundColor: '#32E0C4', // Color de fondo de las barras
               borderColor: '#32E0C4', // Color del borde de las barras
               borderWidth: 1
           }]
       },
       options: {
           responsive: true,
           scales: {
               y: {
                   beginAtZero: true
               }
           }
       }
   });
}