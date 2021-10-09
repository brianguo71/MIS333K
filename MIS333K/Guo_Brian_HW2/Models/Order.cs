using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.ComponentModel.DataAnnotations;

namespace Guo_Brian_HW2.Models
{
    public enum CustomerType { Group, Individual }
    public abstract class Order
    {
        // Price constants
        const Decimal SWEATSHIRT_PRICE = 15.00m;
        const Decimal TSHIRT_PRICE = 10.00m;
        [Display(Name = "Customer Type:")]
        public CustomerType Customer_Type { get; set; }

        [Display(Name = "Customer Code:")]
        [StringLength(6, MinimumLength = 4, ErrorMessage = " Customer code must be 4-6 Characters")]
        [RegularExpression(@"^[a-zA-Z]+$", ErrorMessage = "Customer code may only contain letters")]
        [Required(ErrorMessage = "Specify a Customer Code")]
        public String CustomerCode { get; set; }
        
        [Display(Name = "Number of Sweatshirts:")]
        [Required(ErrorMessage = "Specify a number of sweatshirts")]
        [Range(minimum: 0, maximum: double.PositiveInfinity, ErrorMessage = "Please enter a positive number")]
        [DisplayFormat(DataFormatString = "{0}")]
        // Use Int32? instead of Int32 for [Required] to be implemented properly
        public Int32? NumberOfSweatshirts { get; set; }

        [Display(Name = "Number of T-Shirts:")]
        [Required(ErrorMessage = "Specify a number of t-shirts")]
        [Range(minimum: 0, maximum: double.PositiveInfinity, ErrorMessage = "Please enter a positive number")]
        [DisplayFormat(DataFormatString = "{0}")]
        
        public Int32? NumberOfTshirts { get; set; }
        [Display(Name = "Number of Total Items:")]
        [DisplayFormat(DataFormatString = "{0}")]
        public Int32 TotalItems { get; set; }
        [Display(Name = "Sweatshirt Subtotal:")]
        [DisplayFormat(DataFormatString = "{0:c}")]
        public Decimal SweatshirtSubtotal { get; set; }

        [Display(Name = "T-shirt Subtotal:")]
        [DisplayFormat(DataFormatString = "{0:c}")]
        public Decimal TShirtSubtotal { get; set; }

        [Display(Name = "Subtotal:")]
        [DisplayFormat(DataFormatString = "{0:c}")]
        public Decimal Subtotal { get; set; }

        [Display(Name = "Total:")]
        [DisplayFormat(DataFormatString = "{0:c}")]
        public Decimal Total { get; set; }

        public void CalcSubtotals()
        {
            Int32 Tshirts = (Int32)NumberOfTshirts;
            Int32 Sweatshirts = (Int32)NumberOfSweatshirts;
            TotalItems = Sweatshirts + Tshirts;
            // Throws an exception if total items == 0
            if (TotalItems == 0)
            {
                throw new ArgumentException("Total items cannot be 0");
            }
            SweatshirtSubtotal = Sweatshirts * SWEATSHIRT_PRICE;
            TShirtSubtotal = Tshirts * TSHIRT_PRICE;
            Subtotal = SweatshirtSubtotal + TShirtSubtotal;
        }
    }
}
