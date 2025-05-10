<template>
    <div class="header">
      <div class="header-content">
        <span class="site-name">ESD-Rental Platform</span>
        <div class="nav-right">
          <a class="nav-link">View Items</a>
          <a class="profile-link">
            <img src="../../assets/profile_image.png" alt="Profile" class="profile-image" />
          </a>
        </div>
      </div>
    </div>
  </template>
  
  <style scoped>
  .header {
    width: 100%;
    box-sizing: border-box;
    padding: 1rem 2rem;
  }
  
  .header-content {
    margin: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .site-name {
    font-weight: bold;
    font-size: 2rem;
    color: #688B58;
  }
  
  .nav-right {
    display: flex;
    align-items: center;
    gap: 3rem;
  }
  
  .nav-link {
    text-decoration: none;
    color: #333;
    font-weight: 500;
    font-size: 1.2rem;
    cursor: pointer;
  }
  
  .profile-image {
    width: 3rem;
    height: 3rem;
    border-radius: 50%;
    object-fit: cover;
    cursor: pointer;
  }
  </style>
  