<?php
/*session_start();
$host="localhost";
$usuari="root";
$contrasenya="";
$bbdd="ProjecteFinal";
  
$connexio= new mysqli($host, $usuari, $contrasenya, $bbdd)
  
if ($conn->connect_error) {
    die("Error de connexio " . $conn->connect_error);
}*/
session_start();

$host = "localhost";
$usuari = "root";
$contrasenya = "";
$bbdd = "ProjecteFinal";

$conn = new mysqli($host, $usuari, $contrasenya, $bbdd);

if ($conn->connect_error) {
  die("Error de connexió: " . $conn->connect_error);
}
?>
