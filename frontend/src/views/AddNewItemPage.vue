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
          <TextInput
            label="Pickup:"
            placeholder="Enter pickup location"
            v-model="pickupLocation"
          />
          <TextInput
            label="Return:"
            placeholder="Enter return location"
            v-model="returnLocation"
          />
          <TextAreaInput
            label="Detailed Description: "
            placeholder="Provide a detailed description"
            v-model="description"
          />
        </div>
        <Button label="Add Item" type="submit" @click="handleAdd"></Button>
      </div>
    </div>
  </template>
  
  <script setup>
import { ref } from "vue";
import axios from "axios";
import PageHeader from "../components/common/PageHeader.vue";
import ProfileNavigationBar from "../components/profile_common/ProfileNavigationBar.vue";
import ImageUploader from "../components/ui/ImageUploader.vue";
import TextInput from "../components/ui/TextInput.vue";
import DropdownSelect from "../components/ui/DropdownSelect.vue";
import TextAreaInput from "../components/ui/TextAreaInput.vue";
import Button from "../components/ui/Button.vue";
import { categories } from "../constants/itemCategories";
import { availabilities } from "../constants/availabilities";

const images = ref([]);
const itemName = ref("");
const quantity = ref("");
const category = ref("");
const availability = ref("");
const pickupLocation = ref("");
const returnLocation = ref("");
const description = ref("");

const handleAdd = async () => {
  const token = localStorage.getItem("accessToken");
  
  const bodyData = new FormData();
  bodyData.append("title", itemName.value);
  bodyData.append("quantity", quantity.value);
  bodyData.append("description", description.value);
  bodyData.append("category", category.value);
  bodyData.append("availability", availability.value);
  bodyData.append("pickup_location", pickupLocation.value);
  bodyData.append("return_location", returnLocation.value);

  images.value.forEach((file) => {
    bodyData.append("uploaded_images", file);
  });

  try {
    const response = await axios.post("http://localhost:8000/api/post_item/", bodyData, {
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "multipart/form-data",
      },
    });

    alert("Item added successfully!");
    console.log("Server response:", response.data);
  } catch (error) {
    console.error("Failed to add item:", error.response?.data || error.message);
    alert("Failed to add item");
  }
};
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