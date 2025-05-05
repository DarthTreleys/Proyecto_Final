<?php
session_start();
if (!isset($_SESSION['usuari'])) {
  header('Location: login.php');
  exit;
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Consultoria de Hardening</title>
  <link rel="stylesheet" href="diseny.css">
  <script>
  function cargarContenido(seccion) {
    fetch('contenido.php?seccion=' + seccion)
      .then(res => res.text())
      .then(data => {
        document.getElementById('contenido').innerHTML = data;
      });
  }

  window.onload = function() {
    cargarContenido('inicio');
  </script>
</head>
<body>
  <div class="sidebar">
    <ul>
      <li><a href="inicio.php">Inicio</a></li>
      <li><a href="perfil.php">Perfil</a></li>
      <li><a href="mensajes.php">Mensajes</a></li>
      <li><a href="configuracion.php">Configuración</a></li>
      <li><a href="salir.php">Salir</a></li>
    </ul>
  </div>

  <div class="main-content">
    <div class="contenido-central">
      <h2>Contenido</h2>
      <div id="contenido">
        <p>Cargando contenido...</p>
      </div>
    </div>

    <div class="right-panel">
      <div class="profile-card">
        <h4>Usuari: <?php echo htmlspecialchars($_SESSION['nom']); ?></h4>
          <a href="logout.php">Tancar la sessio</a>
        <div class="profile-pic"></div>
      </div>
      <div class="info-card">
        <h4>Historial</h4>
        <p>Dato 1: ejemplo</p>
        <p>Dato 2: ejemplo</p>
        <p>Dato 3: ejemplo</p>
      </div>
    </div>
  </div>
</body>
</html>
