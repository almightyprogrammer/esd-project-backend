<template>
    <div class="text-input">
      <label v-if="label" class="input-label">{{ label }}</label>
      <input
        :type="type"
        :placeholder="placeholder"
        class="input-field"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
      />
    </div>
  </template>
  
  <script setup>
  defineProps({
    label: String,
    placeholder: String,
    modelValue: String,
    type: {
      type: String,
      default: 'text'
    }
  });
  
  defineEmits(['update:modelValue']);
  </script>
  
  <style scoped>
  .text-input {
    display: flex;
    align-items: center;
    gap: 2rem; 
  }
  
  .input-label {
    min-width: 120px;
    font-weight: bold;
    font-size: 1.2rem;
  }
  
  .input-field {
    flex: 1;
    padding: 0.5rem 0.75rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-size: 1rem;
    outline: none;
  }
  
  .input-field:focus {
    border-color: #666;
  }
  </style>
  