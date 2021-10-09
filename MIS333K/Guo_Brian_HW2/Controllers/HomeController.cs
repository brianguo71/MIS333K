// Name: Brian Guo
// MIS333K 04460
// Homework 2

using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Hosting;
using System.IO;
using Guo_Brian_HW2.Models;

namespace Guo_Brian_HW2.Controllers
{

    public class HomeController : Controller
    {
        private readonly IWebHostEnvironment _environment;
        public HomeController(IWebHostEnvironment environment)
        {
            _environment = environment;
        }
        public IActionResult Index()
        {
            return View();
        }

        public IActionResult CheckoutGroup()
        {
            return View();
        }

        public IActionResult GroupTotals(GroupOrder groupOrder)
        {
            TryValidateModel(groupOrder);
            if(ModelState.IsValid == false)
            {
                return View("CheckoutGroup", groupOrder);
            }
            groupOrder.Customer_Type = CustomerType.Group;
            // If number of T-shirts and sweatshirts == 0, throws an exception
            try
            {
                groupOrder.CalcTotals();
            }
            catch(Exception ex)
            {

                ViewBag.ErrorMessage = ex.Message;
                return View("CheckoutGroup");
            }
            return View("GroupTotals", groupOrder);

        }

        public IActionResult CheckoutIndividual()
        {
            return View();
        }

        public IActionResult IndividualTotals(IndividualOrder individualOrder)
        {
            TryValidateModel(individualOrder);
            if(ModelState.IsValid == false)
            {
                return View("CheckoutIndividual", individualOrder);
            }
            individualOrder.Customer_Type = CustomerType.Individual;
            // If number of T-shirts and sweatshirts == 0, throws an exception
            try
            {
                individualOrder.CalcTotals();
            }
            catch(Exception ex)
            {
                ViewBag.ErrorMessage = ex.Message;
                return View("CheckoutIndividual");
            }
            return View("IndividualTotals", individualOrder);
        }


    }

}
