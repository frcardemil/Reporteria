document.addEventListener('DOMContentLoaded',function() {
  
  // Datos del gráfico
  const data = [100, 200, 150, 300, 250];
  const labels = ['A', 'B', 'C', 'D', 'E'];

  addGrafico('myChart',data,labels);
})
function addGrafico(nameID,listaData,listaNameData){
  const canvas = document.getElementById(nameID);
  const ctx = canvas.getContext('2d');

  // Configuración del gráfico
  const barWidth = 40;
  const barSpacing = 60;
  const baseLine = 350;

  // Dibujar las barras
  listaData.forEach((value, index) => {
    const x = barSpacing * index + barSpacing / 2;
    const y = baseLine - value;
    ctx.fillStyle = 'blue';
    ctx.fillRect(x, y, barWidth, value);

    // Dibujar las etiquetas
    ctx.fillStyle = 'black';
    ctx.fillText(listaNameData[index], x + barWidth / 4, baseLine + 20);
  });
}