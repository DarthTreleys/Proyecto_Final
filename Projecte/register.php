<?php
require 'db.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $nombre  = $_POST['nombre'] ?? '';
  $usuario = $_POST['usuario'] ?? '';
  $clave   = $_POST['clave'] ?? '';

  // Verificar si existe
  $stmt = $pdo->prepare("SELECT id FROM usuarios WHERE usuario = ?");
  $stmt->execute([$usuario]);

  if ($stmt->fetch()) {
    $error = "El usuario ya existe.";
  } else {
    $stmt = $pdo->prepare("INSERT INTO usuarios (nombre, usuario, clave) VALUES (?, ?, ?)");
    $stmt->execute([$nombre, $usuario, $clave]);
    header("Location: login.php");
    exit;
  }
}
?>

<!DOCTYPE html>
<html>
<head>
  <title>Registro</title>
</head>
<body>
  <h2>Crear cuenta</h2>
  <?php if (!empty($error)) echo "<p style='color:red;'>$error</p>"; ?>
  <form method="POST">
    <input type="text" name="nombre" placeholder="Nombre completo" required><br><br>
    <input type="text" name="usuario" placeholder="Usuario" required><br><br>
    <input type="password" name="clave" placeholder="Contraseña" required><br><br>
    <button type="submit">Registrarse</button>
  </form>
  <p><a href="login.php">Volver al login</a></p>
</body>
</html>
