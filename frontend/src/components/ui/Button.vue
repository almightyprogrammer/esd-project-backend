<template>
    <button
      class="green-button"
      @click="$emit('click')"
    >
      {{ label }}
    </button>
  </template>
  
  <script setup>
  defineProps({
    label: {
      type: String,
      required: true
    }
  });
  
  defineEmits(['click']);
  </script>
  
  <style scoped>
  .green-button {
    padding: 0.6rem 1.4rem;
    background-color: #688B58;
    color: white;
    font-size: 1.2rem;
    border: none;
    border-radius: 8px;
    cursor: pointer;
  }
  
  .green-button:hover {
    background-color: #5C7D4E;
  }
  
  </style>
  