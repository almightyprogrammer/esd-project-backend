<template>
    <PageHeader />
    <ProfileNavigationBar />
    <div class="title-container">
      <a class="back-link">< Back to Items</a>
      <h1 class="title">Add New Item</h1>
    </div>
    <div class="content">
      <div class="left-column">
        <ImageUploader
          :images="images"
          @add-image="(img) => images.push(img)"
          @update:images="(imgs) => (images = imgs)"
        />
      </div>
  
      <div class="right-column">
        <div class="fields">
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
        </div>
  
        <Button label="Add Item" type="submit" />
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  import PageHeader from "../components/common/PageHeader.vue";
  import ProfileNavigationBar from "../components/profile_common/ProfileNavigationBar.vue";
  import ImageUploader from "../components/ui/ImageUploader.vue";
  import TextInput from "../components/ui/TextInput.vue";
  import DropdownSelect from "../components/ui/DropdownSelect.vue";
  import TextAreaInput from "../components/ui/TextAreaInput.vue";
  import Button from "../components/ui/Button.vue";
  
  const images = ref([]);
  const itemName = ref("");
  const quantity = ref("");
  const category = ref("");
  const categories = [
    "Event & Party",
    "Board Games",
    "Photography & Video",
    "Electronics & Tech",
    "Arts & Craft",
    "Catering",
    "Tools & DIY",
    "Miscellaneous",
  ];
  const availability = ref("");
  const availabilities = ["Yes", "No"];
  const description = ref("");
  </script>
  
  <style scoped>
  .title-container {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    margin: 2rem;
  }
  
  .back-link {
    font-size: 1rem;
    text-decoration: none;
    cursor: pointer;
  }
  
  .title {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    margin: 0;
    font-size: 2rem;
    font-weight: bold;
  }
  
  .content {
    display: flex;
    justify-content: center;
    align-items: stretch;
    gap: 6rem;
    padding: 2rem;
  }
  
  .left-column {
    flex: 1;
    max-width: 40vw;
  }
  
  .right-column {
    flex: 2;
    max-width: 40vw;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  
  .fields {
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
    flex-grow: 1;
    justify-content: center; 
  }
  </style>
  