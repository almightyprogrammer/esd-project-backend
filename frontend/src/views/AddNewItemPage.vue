AddNewItemPage
<template>
  <PageHeader />
  <ProfileNavigationBar />
  <ImageUploader
    :images="images"
    @add-image="(img) => images.push(img)"
    @update:images="(imgs) => (images = imgs)"
  />
  <TextInput
    label="Item Name:"
    placeholder="Enter item name"
    v-model="itemName"
  />
  <TextInput
    label="Quantity:"
    placeholder="Enter quantity"
    type="number"
    v-model="quantity"
  />
</template>
<script setup>
import { ref } from "vue";
import PageHeader from "../components/common/PageHeader.vue";
import ProfileNavigationBar from "../components/profile_common/ProfileNavigationBar.vue";
import ImageUploader from "../components/ui/ImageUploader.vue";
import TextInput from "../components/ui/TextInput.vue";

const images = ref([]);

function handleImageAdd(newImage) {
  images.value.push(newImage);
}
</script>
