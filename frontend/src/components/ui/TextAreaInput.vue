<template>
    <div class="textarea-input">
      <label v-if="label" class="textarea-label">{{ label }}</label>
      <textarea
        class="textarea-field"
        :placeholder="placeholder"
        :value="modelValue"
        @input="onInput"
        :maxlength="maxLength"
        rows="5"
      ></textarea>
      <div class="char-count">{{ modelValue.length }} / {{ maxLength }}</div>
    </div>
  </template>
  
  <script setup>
  const props = defineProps({
    label: String,
    placeholder: String,
    modelValue: {
      type: String,
      default: ''
    },
    maxLength: {
      type: Number,
      default: 300
    }
  });
  
  const emit = defineEmits(['update:modelValue']);
  
  function onInput(event) {
    emit('update:modelValue', event.target.value);
  }
  </script>
  
  <style scoped>
  .textarea-input {
    display: flex;
    flex-direction: column;
    position: relative;
  }
  
  .textarea-label {
    font-weight: bold;
    font-size: 1.2rem;
    margin-bottom: 0.3rem;
  }
  
  .textarea-field {
    width: 100%;
    padding: 0.5rem 0.75rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-size: 1rem;
    font-family: inherit;
    line-height: 1.2;
    resize: vertical;
    box-sizing: border-box;
    outline: none;
  }
  
  .textarea-field:focus {
    border-color: #666;
  }
  
  .char-count {
    font-size: 1rem;
    color: #999;
    align-self: flex-end;
    margin-top: 0.3rem;
  }
  </style>
  