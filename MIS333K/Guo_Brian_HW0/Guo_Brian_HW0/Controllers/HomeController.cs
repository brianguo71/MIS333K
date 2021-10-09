using Microsoft.AspNetCore.Mvc;
using Guo_Brian_HW0.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Guo_Brian_HW0.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
        [HttpGet]
        public ViewResult RsvpForm()
        {
            return View();
        }
        [HttpPost]
        public IActionResult RsvpForm(GuestResponse guestResponse)
        {
            if (ModelState.IsValid == false) //response is not valid
            {
                return View();
            }

            //if code gets this far, response is correct – add to repository
            Repository.AddResponse(guestResponse);
            return View("Thanks", guestResponse);
        }
        public IActionResult ListResponses()
        {
            IEnumerable<GuestResponse> attendeeList =
            Repository.Responses.Where(r => r.WillAttend ==
           true);
            return View(attendeeList);
        }
    }
}
