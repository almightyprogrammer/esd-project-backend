<template>
  <div class="container">
    <div class="top">
      <span class="images">Images:</span>
      <button class="addButton" @click="triggerFileInput">
        +
        <input
          ref="fileInput"
          type="file"
          accept="image/*"
          multiple
          @change="handleFileUpload"
          hidden
        />
      </button>
    </div>

    <div class="image-viewer">
      <button
        v-if="previewUrls.length"
        class="delete-button"
        @click="deleteImage"
      >
        ×
      </button>
      <img
        v-if="previewUrls.length"
        :src="previewUrls[currentIndex]"
        class="image"
      />
      <div v-else class="placeholder">No images</div>
    </div>

    <div class="navigation-row">
      <button class="arrow" @click="prevImage">‹</button>
      <div class="dot-wrapper">
        <div class="dot-indicator">
          <span
            v-for="(img, i) in previewUrls"
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
import { ref, watch, onBeforeUnmount } from "vue";

const props = defineProps({
  images: {
    type: Array,
    default: () => [],
  },
});
const emit = defineEmits(["add-image", "update:images"]);

const fileInput = ref(null);
const currentIndex = ref(0);
const previewUrls = ref([]);
const objectUrls = ref([]);

// Sync preview URLs
watch(
  () => props.images,
  (newImages) => {
    objectUrls.value.forEach(URL.revokeObjectURL);
    objectUrls.value = [];

    previewUrls.value = newImages.map((file) => {
      if (typeof file === "string") return file;
      const url = URL.createObjectURL(file);
      objectUrls.value.push(url);
      return url;
    });

    if (
      previewUrls.value.length > 0 &&
      currentIndex.value >= previewUrls.value.length
    ) {
      currentIndex.value = previewUrls.value.length - 1;
    }
  },
  { immediate: true }
);

// Clean all remaining url when the component is destroyed
onBeforeUnmount(() => {
  objectUrls.value.forEach(URL.revokeObjectURL);
});

function triggerFileInput() {
  fileInput.value?.click();
}

function handleFileUpload(event) {
  const files = Array.from(event.target.files);
  if (!files.length) return;

  const newImages = [...props.images, ...files];
  emit("update:images", newImages);

  currentIndex.value = newImages.length - 1; //Show the most recently added image

  event.target.value = ""; //Reset to detect images with the same path
}

function deleteImage() {
  const updated = [...props.images];
  updated.splice(currentIndex.value, 1);
  currentIndex.value = Math.max(0, currentIndex.value - 1);
  emit("update:images", updated);
}

function nextImage() {
  if (!previewUrls.value.length) return;
  currentIndex.value = (currentIndex.value + 1) % previewUrls.value.length; // Move back to the lowest index
}

function prevImage() {
  if (!previewUrls.value.length) return;
  currentIndex.value =
    (currentIndex.value - 1 + previewUrls.value.length) %
    previewUrls.value.length; // Move back to the highest index
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
  padding: 0;
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
