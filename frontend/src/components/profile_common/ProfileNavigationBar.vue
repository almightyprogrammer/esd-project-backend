ProfileNavigationBar
<template>
    <div class="dashboard">
      <span class="club-name">Engineering for Sustainable Development</span>
      <div class="links">
        <div class="entry">
        <a>Your Items</a>
        <div class="circle-number">3</div>
      </div>
      <div class="entry">
        <a>Your Bookings</a>
        <div class="circle-number">3</div>
      </div>
      <div class="entry">
        <a>Return Status</a>
        <div class="circle-number">3</div>
      </div>
      </div>
    </div>
    <hr class="divider" />
  </template>
  

<style scoped>
.dashboard {
  display: flex;
  flex-direction: row;
  padding: 1rem 2rem;
  justify-content: space-between;
}

.club-name {
    font-size: 1.5rem;
    font-weight: bold;
}

.links {
  display: flex;
  flex-direction: row;
  gap: 1rem;
  margin-left: 2rem;
}

.entry {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor:pointer;
}

.circle-number {
  width: 1.5rem;
  height: 1.5rem;
  border-radius: 50%;
  background-color: rgba(0,0,0,0.55);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1rem;
}

.divider {
  border: none;
  height: 1px;
  background-color: #000000;
  width: 100%;
  margin: 0;
}

</style>

