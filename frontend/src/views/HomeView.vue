<script setup lang="ts">

</script>

<template>
    <!-- Hero Section -->
    <header class="bg-custom-green text-black py-20">
      <div class="container mx-auto text-center">
        <h2 class="text-5xl font-bold mb-4">Reserva tu cancha en segundos</h2>
        <p class="text-xl mb-8">Juega en las mejores canchas de tu ciudad con RAPITURNO</p>
        <button class="bg-black text-custom-green px-8 py-3 rounded-md text-lg font-semibold hover:bg-gray-800 transition duration-300">
          Reserva Ahora
        </button>
      </div>
    </header>

    <!-- Características -->
    <section class="py-16">
      <div class="container mx-auto">
        <h3 class="text-3xl font-bold text-center mb-12">¿Por qué elegir RAPITURNO?</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="text-center">
            <div class="bg-custom-green text-black rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
              <span class="text-2xl font-bold">5v5</span>
            </div>
            <h4 class="text-xl font-semibold mb-2">Canchas para todos</h4>
            <p>Desde canchas 5v5 hasta 11v11, tenemos el espacio perfecto para tu partido.</p>
          </div>
          <div class="text-center">
            <div class="bg-custom-green text-black rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
              <span class="text-2xl font-bold">📍</span>
            </div>
            <h4 class="text-xl font-semibold mb-2">Múltiples ubicaciones</h4>
            <p>Encuentra canchas cerca de ti en diferentes puntos de la ciudad.</p>
          </div>
          <div class="text-center">
            <div class="bg-custom-green text-black rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
              <span class="text-2xl font-bold">👤</span>
            </div>
            <h4 class="text-xl font-semibold mb-2">Gestión de turnos</h4>
            <p>Administra tus reservas fácilmente desde tu cuenta personal.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Llamado a la acción -->
    <section class="bg-black text-white py-16">
      <div class="container mx-auto text-center">
        <h3 class="text-3xl font-bold mb-4">¿Listo para jugar?</h3>
        <p class="text-xl mb-8">Únete a RAPITURNO y comienza a reservar tus canchas favoritas hoy mismo.</p>
        <button class="bg-custom-green text-black px-8 py-3 rounded-md text-lg font-semibold hover:bg-opacity-90 transition duration-300" data-aos="fade-up">
          Crear Cuenta Gratis
        </button>
      </div>
    </section>


</template>

<style>
/* Definimos el color personalizado */
:root {
  --color-custom-green: #70EB4A;
}

/* Utilizamos la clase de utilidad para el color personalizado */
.bg-custom-green {
  background-color: var(--color-custom-green);
}

.text-custom-green {
  color: var(--color-custom-green);
}
</style>