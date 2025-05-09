AddNewItemPage
<template>
    <PageHeader/>
    <ProfileNavigationBar/>
    <ImageUploader
    :images="images"
    @add-image="img => images.push(img)"
    @update:images="imgs => images = imgs"
  />
</template>
<script setup>
    import { ref } from 'vue';
    import PageHeader from '../components/common/PageHeader.vue';
    import ProfileNavigationBar from '../components/profile_common/ProfileNavigationBar.vue';
    import ImageUploader from '../components/inputs/ImageUploader.vue';
    
    const images = ref([]);

    function handleImageAdd(newImage) {
        images.value.push(newImage);
    }
</script>
