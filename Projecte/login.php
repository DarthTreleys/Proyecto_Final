<?php
session_start();
require 'db.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $usuario = $_POST['usuario'] ?? '';
  $clave = $_POST['clave'] ?? '';

  $stmt = $pdo->prepare("SELECT * FROM usuarios WHERE usuario = ? AND clave = ?");
  $stmt->execute([$usuario, $clave]);
  $user = $stmt->fetch();

  if ($user) {
    $_SESSION['usuario'] = $user['usuario'];
    $_SESSION['nombre'] = $user['nombre'];
    header('Location: index.php');
    exit;
  } else {
    $error = "Usuario o contraseña incorrectos.";
  }
}
?>

<!DOCTYPE html>
<html>
<head>
  <title>Iniciar sesión</title>
</head>
<body>
  <h2>Login</h2>
  <?php if (!empty($error)) echo "<p style='color:red;'>$error</p>"; ?>
  <form method="POST">
    <input type="text" name="usuario" placeholder="Usuario" required><br><br>
    <input type="password" name="clave" placeholder="Contraseña" required><br><br>
    <button type="submit">Entrar</button>
  </form>
  <p>¿No tienes cuenta? <a href="register.php">Regístrate aquí</a></p>
</body>
</html>