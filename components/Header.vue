<template>
  <header
    :class="[
      'overflow-hidden font-light font-press text-[#f5f5f5] mb-[5vh] text-center',
      'break-words text-[20px] sm:text-[30px] md:text-[40px]',
      hasAnimation ? 'border-r-2 border-[#f5f5f5] animate-typing' : '',
    ]"
    :style="{ width: hasAnimation ? 'fit-content' : 'auto' }"
  >
    Identifier Readability
  </header>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
  hasAnimation: {
    type: Boolean,
    default: false, 
  },
});
</script>

<style scoped>

@keyframes typing {
  from {
    width: 0;
  }
  to {
    width: 20ch; 
  }
}

@keyframes blink {
  0%, 20% { 
    border-color: #f5f5f5; 
  }
  21%, 40% { 
    border-color: transparent; 
  }
  41%, 60% { 
    border-color: #f5f5f5; 
  }
  61%, 80% { 
    border-color: transparent; 
  }
  81%, 100% { 
    border-color: transparent; 
  }
}

.animate-typing {
  animation: 
    typing 3s steps(20, end), 
    blink 4s steps(20) 3s 1 normal forwards; 
  width: 20ch; 
  white-space: nowrap;
  overflow: hidden;
}
</style>
