package controller;

import entity.Post;
import org.apache.catalina.User;
import service.PostService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/postTexts")
public class PostController {
    @Autowired
    private  PostService postService;

    @GetMapping
    public List<Post> getPostTexts() {
        return postService.GetAllPostTexts();
    }

    @PostMapping
    public Post createPostText(@RequestBody Post post){
        return postService.SavePostText(post);
    }
}
