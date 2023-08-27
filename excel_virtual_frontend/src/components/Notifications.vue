<template>
  <div 
    id="toast-success" class="flex items-center w-full max-w-xs p-4 mb-4 text-gray-500 bg-white rounded-lg shadow dark:text-gray-400 dark:bg-gray-800" role="alert">
    <font-awesome-icon :icon="icon[status].icon" :style="{color: icon[status].color}" size="xl" class=" mr-3" />
    <slot class="ml-3 text-sm font-normal"></slot>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const icon = ref({
  success: {icon: 'fa-solid fa-circle-check', color: '#1f9821'},
  warning: {icon: 'fa-solid fa-circle-exclamation', color: '#24519e'},
  error: {icon: 'fa-solid fa-triangle-exclamation', color: '#c43636'}
})

defineProps({
  status: String
})

</script>

<style scoped>

</style>