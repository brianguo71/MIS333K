using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Hosting;
using System.IO;


namespace Guo_Brian_HW1.Controllers
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
        public IActionResult ReturnAFile()
        {
            string path = _environment.WebRootPath + "/files/BrianGuoResume.pdf";
            var stream = new FileStream(path, FileMode.Open);
            return File(stream, "application/pdf", "BrianGuoResume.pdf");
        }
        public IActionResult Hobbies()
        {
            return View();
        }
        public IActionResult About()
        {
            return View();
        }
    }

}