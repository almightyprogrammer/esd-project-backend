<template>
  <div class="container">
    <!-- Top bar -->
    <div class="top">
      <span class="images">Images:</span>
      <button class="addButton" @click="triggerFileInput">
        +
        <input
          ref="fileInput"
          type="file"
          accept="image/*"
          @change="handleFileUpload"
          hidden
        />
      </button>
    </div>

    <!-- Image viewer -->
    <div class="image-viewer">
      <button
        v-if="localImages.length"
        class="delete-button"
        @click="deleteImage"
      >
        ×
      </button>
      <img
        v-if="localImages.length"
        :src="localImages[currentIndex]"
        class="image"
      />
      <div v-else class="placeholder">No images</div>
    </div>

    <!-- Navigation row -->
    <div class="navigation-row">
      <button class="arrow" @click="prevImage">‹</button>

      <div class="dot-wrapper">
        <div class="dot-indicator">
          <span
            v-for="(img, i) in localImages"
            :key="i"
            class="dot"
            :class="{ active: i === currentIndex }"
          ></span>
        </div>
      </div>

      <button class="arrow" @click="nextImage">›</button>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";

const props = defineProps({
  images: {
    type: Array,
    default: () => [],
  },
});

const emit = defineEmits(["add-image", "update:images"]);

const fileInput = ref(null);
const currentIndex = ref(0);
const localImages = ref([]);

// Sync localImages with parent prop
watch(
  () => props.images,
  (newImages) => {
    localImages.value = [...newImages];
    if (newImages.length > 0 && currentIndex.value >= newImages.length) {
      currentIndex.value = newImages.length - 1;
    }
  },
  { immediate: true }
);

// Trigger file input
function triggerFileInput() {
  fileInput.value?.click();
}

// Handle file upload
function handleFileUpload(event) {
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = () => {
    const imageData = reader.result;
    localImages.value.push(imageData);
    currentIndex.value = localImages.value.length - 1;
    emit("add-image", imageData);
  };
  reader.readAsDataURL(file);
}

// Delete current image
function deleteImage() {
  localImages.value.splice(currentIndex.value, 1);
  currentIndex.value = Math.max(0, currentIndex.value - 1);
  emit("update:images", [...localImages.value]);
}

// Navigation
function nextImage() {
  if (localImages.value.length === 0) return;
  currentIndex.value = (currentIndex.value + 1) % localImages.value.length;
}

function prevImage() {
  if (localImages.value.length === 0) return;
  currentIndex.value =
    (currentIndex.value - 1 + localImages.value.length) %
    localImages.value.length;
}
</script>

<style scoped>
.container {
  width: 40vw;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 1.2rem;
  font-weight: bold;
}

.addButton {
  font-size: 2rem;
  background: none;
  border: none;
  cursor: pointer;
}

.image-viewer {
  position: relative;
  width: 100%;
  aspect-ratio: 4 / 3;
  background-color: #f3f3f3;
  border: 1px solid #ccc;
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.placeholder {
  color: #aaa;
  font-style: italic;
}

.delete-button {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  background: rgba(255, 255, 255, 0.9);
  border: none;
  border-radius: 50%;
  font-size: 1.2rem;
  width: 1.8rem;
  height: 1.8rem;
  cursor: pointer;
  z-index: 2;
}

.navigation-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.arrow {
  background: none;
  border: none;
  font-size: 1.8rem;
  padding: 0.3rem 0.6rem;
  cursor: pointer;
  color: #333;
}

.dot-wrapper {
  flex-grow: 1;
  display: flex;
  justify-content: center;
}

.dot-indicator {
  display: flex;
  gap: 0.4rem;
  align-items: center;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: #ccc;
  transition: all 0.3s ease;
}

.dot.active {
  background-color: #000;
  transform: scale(1.6);
}
</style>
