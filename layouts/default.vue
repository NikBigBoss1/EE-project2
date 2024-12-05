<template>
  <div class="app-wrapper">
    <div class="app-background"></div>
    <div class="container">
      <slot />
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
/* .body {
  background-color: black;
} */
.app-wrapper {
  background-color: black;
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.container {
  position: relative;
  width: 100%;
  height: 100%;
  margin: 0 auto;
  overflow: hidden;
}

.app-background {
  position: absolute;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    45deg,
    rgba(37, 165, 44, 0.5),
    rgba(221, 224, 42, 0.5)
  );
  background-size: cover;
  background-position: center;
  filter: blur(3px);
}
</style>
