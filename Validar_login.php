<?php
session_start();
include('conexion.php');

//verificar conexion con la BBDD
if (!$conn) {
    die("Error al conectarse con la base de datos");
}

// Obtener datos del formulario
$username = $_POST['username'];
$password = $_POST['password'];

// Consulta para verificar el usuario y rol
$sql = "SELECT u.rol FROM usuarios u JOIN Rol r ON u.rol = r.ID WHERE u.username = ? AND u.Password = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ss", $username, $password);
$stmt->execute();
$stmt->bind_result($rol);
$stmt->fetch();

if ($rol) {
    $_SESSION['username'] = $username;
    $_SESSION['rol'] = $rol;

    // Redireccionar según el rol
    if ($rol === 2) {
        header("Location: dashboard_tecnico.php");
    } elseif ($rol === 1) {
        header("Location: dashboard_cliente.php");
    }
} else {
    // Si las credenciales no son válidas
    echo "<script>alert(' ¡¡Eh tú!!, deja ya las inyecciones de SQL, ponte a hacer cables de red o comprate un perro y deja de molestarnos y si te echas novia y desapareces de la informática mejor'); window.location.href = 'login.php';</script>";
    
}

$stmt->close();
$conn->close();
?>