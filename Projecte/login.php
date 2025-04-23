<?php
session_start();
require 'db.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $usuari = $_POST['usuari'] ?? '';
  $passwd = $_POST['passwd'] ?? '';

  $stmt = $pdo->prepare("SELECT * FROM usuaris WHERE User = ? AND Password = ?");
  $stmt->execute([$usuario, $passwd]);
  $user = $stmt->fetch();

  if ($user) {
    $_SESSION['usuari'] = $user['usuari'];
    $_SESSION['nom'] = $user['nom'];
    header('Location: index.php');
    exit;
  } else {
    $error = "Usuari o contrasenya incorrecte.";
  }
}
?>

<!DOCTYPE html>
<html>
<head>
  <title>Iniciar sessio</title>
</head>
<body>
  <h2>Login</h2>
  <?php if (!empty($error)) echo "<p style='color:red;'>$error</p>"; ?>
  <form method="POST">
    <input type="text" name="usuari" placeholder="Usuari" required><br><br>
    <input type="password" name="passwd" placeholder="Contrasenya" required><br><br>
    <button type="submit">Entrar</button>
  </form>
  <p>¿No Tens Compte? <a href="register.php">Crea-te'l aqui</a></p>
</body>
</html>
