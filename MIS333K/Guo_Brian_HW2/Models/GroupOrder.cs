using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.ComponentModel.DataAnnotations;

namespace Guo_Brian_HW2.Models
{
    public class GroupOrder : Order
    {
        [Display(Name = " Is this a preferred customer?")]
        public bool PreferredCustomer { get; set; }

        [Display(Name = "Setup Fee:")]
        [DisplayFormat(DataFormatString = "{0:c}")]
        [Range(minimum: 0, maximum: double.PositiveInfinity, ErrorMessage = "Please enter a positive number")]
        [Required(ErrorMessage = "Setup Fee is required")]
        // Decimal? instead of Decimal for [Required] to be implemented properly
        public Decimal? SetupFee { get; set; }

        public void CalcTotals()
        {
            // Convert Setup from Decimal? to Decimal to be usable when calculating Total
            Decimal Setup = (Decimal)SetupFee;
            base.CalcSubtotals();
            if (PreferredCustomer == true || Subtotal > 5000) 
            {
                PreferredCustomer = true;
                SetupFee = 0;
                Total = Subtotal;
            }
            else
            {
                Total = Subtotal + Setup;
            }

        }
    }
}
