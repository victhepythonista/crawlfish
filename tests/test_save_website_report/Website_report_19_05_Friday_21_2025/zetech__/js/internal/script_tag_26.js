
    var isPopupVisible = false;
    var isPopupClosed = localStorage.getItem('isPopupClosed');

    // Function to open the popup
    function openPopup() {
      document.getElementById('popup').style.display = 'block';
      document.getElementById('overlay').style.display = 'block';
      isPopupVisible = true;
    }

    // Function to close the popup
    function closePopup() {
      document.getElementById('popup').style.display = 'none';
      document.getElementById('overlay').style.display = 'none';
      isPopupVisible = false;
    }

    // Check if the popup should be opened on page load
    window.onload = function () {
      if (!isPopupVisible && isPopupClosed !== 'true') {
        openPopup();
      }
    };
  