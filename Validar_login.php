<?php
session_start();
include('db.php');

//verificar conexion con la BBDD
if (!$conn) {
    die("Error al conectar-se con la base de dades");
}

// Obtener datos del formulario
$username = $_POST['username'];
$password = $_POST['password'];

// Consulta para verificar el usuario y rol
$sql = "SELECT * FROM usuaris WHERE User = ? AND Password = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ss", $username, $password);
$stmt->execute();
$stmt->bind_result($user);
$stmt->fetch();

if ($user) {
    //Si hay coincidencia
    header("Location: index.php");
} else {
    // Si las credenciales no son válidas
    echo "<script>alert(' Disculpi, però les credencials que ha donat no son correctes o no estan registrades'); window.location.href = 'login.php';</script>";
    
}

$stmt->close();
$conn->close();
?>
