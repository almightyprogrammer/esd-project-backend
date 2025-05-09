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
  <DropdownSelect
    label="Category: "
    :options="categories"
    v-model="category"
  />
  <DropdownSelect
    label="Availability: "
    :options="availabilities"
    v-model="availability"
  />
  <TextAreaInput
    label="Detailed Description: "
    placeholder="Provide a detailed description"
    v-model="description"
  />

</template>
<script setup>
import { ref } from "vue";
import PageHeader from "../components/common/PageHeader.vue";
import ProfileNavigationBar from "../components/profile_common/ProfileNavigationBar.vue";
import ImageUploader from "../components/ui/ImageUploader.vue";
import TextInput from "../components/ui/TextInput.vue";
import DropdownSelect from '../components/ui/DropdownSelect.vue';
import TextAreaInput from "../components/ui/TextAreaInput.vue";

const images = ref([]);

const category = ref('');
const categories = ['Event & Party', 'Board Games', 'Photography & Video','Electronics & Tech','Arts & Craft','Catering','Tools & DIY','Miscellaneous'];

const availability = ref('');
const availabilities =['Yes', 'No'];

const description = ref('');

function handleImageAdd(newImage) {
  images.value.push(newImage);
}
</script>
