<template>
    <div class="text-input">
      <label v-if="label" class="input-label">{{ label }}</label>
      <select
        class="input-field"
        :value="modelValue"
        @change="$emit('update:modelValue', $event.target.value)"
      >
        <option disabled value="" class="placeholder">Please select an option</option>
        <option
          v-for="(option, index) in options"
          :key="index"
          :value="option"
        >
          {{ option }}
        </option>
      </select>
    </div>
  </template>
  
  <script setup>
  defineProps({
    label: String,
    options: {
      type: Array,
      required: true
    },
    modelValue: String,
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
    appearance: none;
  }
  
  .input-field:focus {
    border-color: #666;
  }
  
  .placeholder {
    color: #999;
  }
  </style>
  