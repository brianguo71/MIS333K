using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.ComponentModel.DataAnnotations;

namespace Guo_Brian_HW2.Models
{ 
    public class IndividualOrder : Order
    {
    // Rate and fee constants
    const Decimal SALES_TAX_RATE = 0.0875m;
    const Decimal SWEATSHIRT_FEE = 2.5m;
    const Decimal TSHIRT_FEE = 2.00m;

    [Display(Name = "Customer Name:")]
    [Required(ErrorMessage = "Customer name is required")]
    public String CustomerName { get; set; }


    [Display(Name = "Processing Fee:")]
    [DisplayFormat(DataFormatString = "{0:c}")]
    public Decimal ProcessingFee { get; set; }


    [Display(Name = "Sales Tax:")]
    [DisplayFormat(DataFormatString = "{0:c}")]
    public Decimal SalesTax { get; set; }
    public void CalcTotals()
    {
        base.CalcSubtotals();
        // Convert Int32?s to Int32 to be usable for calculating ProcessingFee
        Int32 Tshirts = (Int32)NumberOfTshirts;
        Int32 Sweatshirts = (Int32)NumberOfSweatshirts;
        ProcessingFee = (Sweatshirts * SWEATSHIRT_FEE) + (Tshirts * TSHIRT_FEE);
        SalesTax = (Subtotal + ProcessingFee) * SALES_TAX_RATE;
        Total = Subtotal + ProcessingFee + SalesTax;
    }

    }
}
